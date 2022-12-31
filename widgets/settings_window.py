from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.resize(400, 300)