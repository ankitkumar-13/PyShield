import sys
from mainwindow import QApplication, MainWindow
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox
import socket
import threading
from scapy.all import sniff, IP, TCP, UDP
import subprocess
from threading import Timer
import datetime
import json
import os

class FirewallSignals(QObject):
    log_added = Signal(str)

class Firewall:
    def __init__(self, signals):
        self.signals = signals
        self.rules = {
            'src_ip': set(),
            'dst_port': set(),
            'domains': set()
        }
        self.domain_ips = {}
        self.is_running = False
        self.sniffer_thread = None
        self.stop_flag = threading.Event()
        self.windows_firewall_rules = set()
        self.load_existing_rules()

    def resolve_domain(self, domain):
        try:
            ips = socket.gethostbyname_ex(domain)[2]
            self.domain_ips[domain] = ips
            return ips
        except Exception as e:
            self.log(f"DNS resolution failed for {domain}: {str(e)}")
            return []

    import subprocess

    def add_windows_firewall_rule(self, ip):
      try:
        rule_name = f"BlockPyShield_{ip}"
        
        # Avoid adding the same rule again
        if rule_name in self.windows_firewall_rules:
            return True

        # Run the netsh command to add the rule
        result = subprocess.run(
            [
                'netsh', 'advfirewall', 'firewall', 'add', 'rule',
                f'name={rule_name}',
                'dir=in', 'action=block',
                f'remoteip={ip}'
            ],
            check=True,
            capture_output=True,
            text=True,
            creationflags=subprocess.CREATE_NO_WINDOW
        )

        # Debug output
        print("NETSH OUTPUT:", result.stdout)
        print("NETSH ERRORS:", result.stderr)

        # Track added rule
        self.windows_firewall_rules.add(rule_name)
        return True

      except subprocess.CalledProcessError as e:
        print(f"NETSH FAILED: {e.stderr}")  # Debug
        self.log(f"Failed to add Windows firewall rule: {str(e)}")
        return False

    def packet_handler(self, packet):
      if IP in packet:
        src_ip = packet[IP].src
        if src_ip in self.rules['src_ip']:
            self.log(f"Blocked packet from {src_ip}")
            return "Blocked"  # Actively drop the packet
            

    def refresh_domain_blocks(self):
        for domain in self.rules['domains']:
            ips = self.resolve_domain(domain)
            for ip in ips:
                if ip not in self.rules['src_ip']:
                    self.rules['src_ip'].add(ip)
                    self.add_windows_firewall_rule(ip)
        
        if self.is_running:
            Timer(300, self.refresh_domain_blocks).start()

    def load_existing_rules(self):
        try:
            if os.path.exists('firewall_rules.json'):
                with open('firewall_rules.json', 'r') as f:
                    rules = json.load(f)
                    self.rules['src_ip'] = set(rules.get('src_ip', []))
                    self.rules['dst_port'] = set(map(int, rules.get('dst_port', [])))
                    self.rules['domains'] = set(rules.get('domains', []))
                    
                    for ip in self.rules['src_ip']:
                        self.add_windows_firewall_rule(ip)
        except Exception as e:
            self.log("Error loading rules: " + str(e))

    def cleanup_firewall_rules(self):
        for rule_name in list(self.windows_firewall_rules):
            try:
                subprocess.run(
                    f'netsh advfirewall firewall delete rule name="{rule_name}"',
                    shell=True,
                    check=True,
                    creationflags=subprocess.CREATE_NO_WINDOW
                )
                self.windows_firewall_rules.remove(rule_name)
            except subprocess.CalledProcessError as e:
                self.log(f"Failed to remove rule {rule_name}: {str(e)}")

    def save_rules_to_file(self):
        try:
            with open('firewall_rules.json', 'w') as f:
                json.dump({
                    'src_ip': list(self.rules['src_ip']),
                    'dst_port': list(map(str, self.rules['dst_port'])),
                    'domains': list(self.rules['domains'])
                }, f)
        except Exception as e:
            self.log("Error saving rules: " + str(e))

    def add_rule(self, rule_type, value):
        if rule_type == 'dst_port':
            try:
                value = int(value)
            except ValueError:
                QMessageBox.warning(None, "Invalid Input", "Please enter a valid port number.")
                self.log("Invalid port number: " + str(value))
                return False

        if rule_type == 'src_ip' and any(c.isalpha() for c in value):
            self.rules['domains'].add(value)
            ips = self.resolve_domain(value)
            if not ips:
                QMessageBox.warning(None, "Resolution Failed", f"Could not resolve {value}")
                return False
            
            for ip in ips:
                self.rules['src_ip'].add(ip)
                self.add_windows_firewall_rule(ip)
            
            self.log(f"Resolved {value} to IPs: {', '.join(ips)}")
        else:
            self.rules[rule_type].add(value)
            if rule_type == 'src_ip':
                self.add_windows_firewall_rule(value)
        
        self.save_rules_to_file()
        self.log("Added " + str(rule_type) + " rule: " + str(value))
        QMessageBox.information(None, "Success", "Rule added successfully.")
        return True

    def packet_handler(self, packet):
        if IP in packet:
            src_ip = packet[IP].src
            dst_port = None
            
            if TCP in packet:
                dst_port = packet[TCP].dport
            elif UDP in packet:
                dst_port = packet[UDP].dport
            
            if src_ip in self.rules['src_ip']:
                self.log("Blocked packet from " + str(src_ip) + " (blacklisted IP)")
                return
            
            if dst_port in self.rules['dst_port']:
                self.log("Blocked packet to port " + str(dst_port) + " (blacklisted port)")
                return
            
            protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
            self.log(f"Allowed {protocol} packet: {src_ip} -> {packet[IP].dst}{':' + str(dst_port) if dst_port else ''}")

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.sniffer_thread = threading.Thread(target=self._start_sniffing)
            self.sniffer_thread.daemon = True
            self.sniffer_thread.start()
            self.refresh_domain_blocks()
            self.log("Firewall started")

    def _start_sniffing(self):
        try:
            sniff(prn=self.packet_handler, store=0, filter="ip", 
                  stop_filter=lambda _: self.stop_flag.is_set())
        except Exception as e:
            self.log("Sniffing error: " + str(e))
            self.stop()

    def stop(self):
        if self.is_running:
            self.stop_flag.set()
            if self.sniffer_thread:
                self.sniffer_thread.join(timeout=2)
            self.is_running = False
            self.log("Firewall stopped")

    def log(self, message):
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log_message = f"[{timestamp}] {message}"
        self.signals.log_added.emit(log_message)
        
        try:
            with open('firewall.txt', 'a') as f:
                f.write(log_message + '\n')
        except Exception as e:
            print(f"Error writing to log file: {e}")

class MainWindowExtended(MainWindow):
    def __init__(self):
        super().__init__()
        self.firewall_signals = FirewallSignals()
        self.firewall = Firewall(self.firewall_signals)
        
        self.firewall_signals.log_added.connect(self.update_logs)
        self.ui.pushButton_5.clicked.connect(self.add_rule)
        self.ui.pushButton_4.clicked.connect(self.confirmation_yes_or_no)
        
    def start_firewall(self):
        super().start_firewall()
        self.firewall.start()
        
    def stop_firewall(self):
        super().stop_firewall()
        self.firewall.stop()
        
    def add_rule(self):
        rule_type = self.ui.comboBox.currentText()
        value = self.ui.lineEdit.text().strip()
        if value:
            self.firewall.add_rule(rule_type, value)
            self.ui.lineEdit.clear()
        
    def show_info_popup(self):
        rules_text = "Current Firewall Rules:\n\n"
        rules_text += "Blocked Source IPs:\n"
        rules_text += "\n".join(sorted(self.firewall.rules['src_ip'])) or "None\n"
        rules_text += "\nBlocked Destination Ports:\n"
        rules_text += "\n".join(map(str, sorted(self.firewall.rules['dst_port']))) or "None"
        
        QMessageBox.information(self, "Rules Set", rules_text)
        
    def update_logs(self, message):
        self.ui.logsView.appendPlainText(message)
    
    def confirmation_yes_or_no(self):
        result = QMessageBox.question(self, "Confirm Action", 
                                    "Are you sure you want to clear all logs?",
                                    QMessageBox.StandardButton.Yes, 
                                    QMessageBox.StandardButton.No)
        if result == QMessageBox.StandardButton.Yes:
            self.ui.logsView.clear()
            self.update_logs("Logs Cleared!\n")

if __name__ == "__main__":
    if os.name == 'nt':  # Windows
        import ctypes
        if not ctypes.windll.shell32.IsUserAnAdmin():
            # Re-run as admin
            ctypes.windll.shell32.ShellExecuteW(None, "runas", sys.executable, " ".join(sys.argv), None, 1)
            sys.exit()
    
    app = QApplication(sys.argv)
    widget = MainWindowExtended()
    widget.show()
    sys.exit(app.exec())
