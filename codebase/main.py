import sys
from mainwindow import QApplication, MainWindow
from PySide6.QtCore import QObject, Signal
from PySide6.QtWidgets import QMessageBox

import threading
from scapy.all import sniff, IP, TCP, UDP

import datetime
import json
import os   #For checking existing files;

class FirewallSignals(QObject):
    log_added = Signal(str) #String type values passed to the signal.

class Firewall:
    def __init__(self, signals):
        self.signals = signals
        self.rules = {
            'src_ip': set(),
            'dst_port': set()
        }
        self.is_running = False
        self.sniffer_thread = None
        self.stop_flag = threading.Event()
        self.load_existing_rules()

    def load_existing_rules(self):
        try:
            if os.path.exists('firewall_rules.json'):
                with open('firewall_rules.json', 'r') as f:
                    rules = json.load(f)
                    self.rules['src_ip'] = set(rules.get('src_ip', []))
                    self.rules['dst_port'] = set(map(int, rules.get('dst_port', [])))
        except Exception as e:
            self.log("Error loading rules: "+  str(e))

    def save_rules_to_file(self):
        try:
            with open('firewall_rules.json', 'w') as f:
                json.dump({
                    'src_ip': list(self.rules['src_ip']),
                    'dst_port': list(map(str, self.rules['dst_port']))
                }, f)
        except Exception as e:
            self.log("Error saving rules: "+  str(e)) 

    def add_rule(self, rule_type, value):   # Returns a bool whether the rule added or not.
        if rule_type == 'dst_port':
            try:
                value = int(value)
            except ValueError:
                QMessageBox.warning(None, "Invalid Input", "Please enter a valid port number.")
                self.log("Invalid port number: " + str(value))
                return False
        
        self.rules[rule_type].add(value)
        self.save_rules_to_file()
        self.log("Added " + str(rule_type) + "rule: " + str(value))
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
            
            # Log allowed packets
            protocol = "TCP" if TCP in packet else "UDP" if UDP in packet else "Other"
            self.log("Allowed " +str(protocol) + " packet: " + str(src_ip) + " -> " + str(packet[IP].dst) + ((":" + str(dst_port)) if dst_port else ""))

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.sniffer_thread = threading.Thread(target=self._start_sniffing)
            self.sniffer_thread.daemon = True
            self.sniffer_thread.start()
            self.log("Firewall started")

    def _start_sniffing(self):
        try:
            sniff(prn=self.packet_handler, store=0, filter="ip", 
                  stop_filter=lambda _ :self.stop_flag.is_set())
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
        log_message = "[" + str(timestamp) +"] " + str(message)
        self.signals.log_added.emit(log_message)
        
        try:
            with open('firewall.log', 'a') as f:
                f.write(log_message + '\n')
        except Exception as e:
            print(f"Error writing to log file: {e}")

class MainWindowExtended(MainWindow):
    def __init__(self):
        super().__init__()
        self.firewall_signals = FirewallSignals()
        self.firewall = Firewall(self.firewall_signals)
        
        # Connect signals
        self.firewall_signals.log_added.connect(self.update_logs)
        self.ui.pushButton_5.clicked.connect(self.add_rule)
        
    def start_firewall(self):
        super().start_firewall()    #Updates the button to enabled amd disabled mode
        self.firewall.start()
        
    def stop_firewall(self):
        super().stop_firewall()  #Updates the button to enabled amd disabled mode
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

if __name__ == "__main__":
    app = QApplication(sys.argv)
    widget = MainWindowExtended()
    widget.show()
    sys.exit(app.exec())