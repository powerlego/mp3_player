from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSettings


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        
        self.setWindowTitle("Settings")
        self.resize(1024, 768)
        self.setModal(True)
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.settingsView = QtWidgets.QTreeWidget()
        self.settingsView.setHeaderHidden(True)
        self.settingsView.setAnimated(True)
        self.settingsView.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.settingsView.setObjectName("settingsView")
        self.settingsView.setSizePolicy(QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vbox = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Theme")
        self.vbox.addWidget(self.label)
        self.vboxWidget = QtWidgets.QWidget()
        self.vboxWidget.setSizePolicy(QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Expanding)
        self.vboxWidget.setLayout(self.vbox)
        self.splitter.addWidget(self.settingsView)
        self.splitter.addWidget(self.vboxWidget)
        self.splitter.setStretchFactor(0,0)
        self.splitter.setStretchFactor(1,5)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)
        self.settings = QSettings()
        self.theme = self.settings.value("theme", "dark")
        self.language = self.settings.value("language", "en")
        self.volume = self.settings.value("volume", 50)
        print(self.theme)
        # if(self.theme == "dark"):
        #     self.setStyleSheet(
        #         "background-color: #333333; color: #ffffff;}"
        #         "QTreeView#settingsView{background-color: #424242; border:3px inset #4d4d4d; color: #ffffff;}"
        #     )
        # else:
        #     self.setStyleSheet(
        #         "QDialog{background-color: #ffffff; color: #000000;}"
        #         "QTreeView#settingsView{background-color: #e0e0e0; border: 1px inset #ededed; color: #000000;}"
        #     )

    def closeEvent(self, event):
        self.write_settings()
        self.settings.sync()
        event.accept()

    def write_settings(self):
        self.settings.setValue("theme", self.theme)
        self.settings.setValue("language", self.language)
        self.settings.setValue("volume", self.volume)
