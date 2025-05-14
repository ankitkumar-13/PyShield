# This Python file uses the following encoding: utf-8

from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtCore import QEvent

# Important:
# You need to run the following command to generate the ui_form.py file
#     pyside6-uic form.ui -o ui_form.py, or
#     pyside2-uic form.ui -o ui_form.py
from ui_form import Ui_MainWindow

class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton_3.clicked.connect(self.show_info_popup)
        self.ui.pushButton_4.clicked.connect(self.show_confirmation_popup)

        self.ui.pushButton.clicked.connect(self.start_firewall)
        self.ui.pushButton_2.clicked.connect(self.stop_firewall)
    #Code taken since on direct disable we can't remove the hover effect before disabling the button.
    def _clear_hover(self, button):
            # 1) Fake leave event
            leave_ev = QEvent(QEvent.Leave)
            QApplication.sendEvent(button, leave_ev)
            # 2) Recompute style
            button.style().unpolish(button)
            button.style().polish(button)
            # 3) Repaint
            button.update()

    def start_firewall(self):
        self.ui.pushButton_2.setDisabled(False)
        self.ui.pushButton.setDisabled(True)
        self._clear_hover(self.ui.pushButton)

    def stop_firewall(self):
        self.ui.pushButton.setDisabled(False)
        self.ui.pushButton_2.setDisabled(True)
        self._clear_hover(self.ui.pushButton_2)

    def show_info_popup(self):
        QMessageBox.information(self, "Rules Set", "All the defined rules will get shown here.")

    def show_confirmation_popup(self):
        QMessageBox.question(self, "Confirm Action", "Are you sure you want to clear all logs ?", QMessageBox.StandardButton.Yes, QMessageBox.StandardButton.No)
