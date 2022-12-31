from PySide6 import QtWidgets
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSettings

class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Settings")
        self.resize(400, 300)
        self.setModal(True)
        self.settings = QSettings(QSettings.UserScope, "MP3 Player", "settings")
        self.theme = self.settings.value("theme", "dark")
        self.language = self.settings.value("language", "en")
        
    def closeEvent(self,event):
        self.write_settings()
        event.accept()
        
        
    def write_settings(self):
        self.settings.setValue("theme", self.theme)
        self.settings.setValue("language", self.language)
        self.settings.setValue("volume", self.volume)