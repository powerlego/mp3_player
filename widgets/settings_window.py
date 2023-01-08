from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import QSettings


class SettingsWindow(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()
        self.settingsList.setFocus()
        self.settings = QSettings()
        self.read_settings()

    def build_ui(self):
        self.setWindowTitle("Settings")
        self.resize(1024, 768)
        self.setModal(True)
        self.splitter = QtWidgets.QSplitter()
        self.splitter.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.settingsList = QtWidgets.QListWidget()
        self.settingsList.setSizePolicy(
            QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding
        )
        self.settingsList.setSpacing(2)
        self.settingsList.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.settingsList.setObjectName("settingsList")
        self.settingsList.setSelectionMode(
            QtWidgets.QAbstractItemView.SelectionMode.SingleSelection
        )
        self.add_settings(self.mainSettings())
        self.settingsList.setCurrentRow(0)
        self.settingsList.currentItemChanged.connect(self.on_current_item_changed)
        self.settingsArea = QtWidgets.QStackedLayout()
        self.settingsArea.addWidget(GeneralSettings())
        self.settingsArea.addWidget(AppearanceSettings())
        self.settingsArea.addWidget(AudioSettings())
        self.settingsAreaWidget = QtWidgets.QWidget()
        self.settingsAreaWidget.setLayout(self.settingsArea)
        self.splitter.addWidget(self.settingsList)
        self.splitter.addWidget(self.settingsAreaWidget)
        self.splitter.setStretchFactor(0, 0)
        self.splitter.setStretchFactor(1, 5)
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.splitter)
        self.setLayout(self.layout)

    def on_current_item_changed(
        self, current: QtWidgets.QListWidgetItem, previous: QtWidgets.QListWidgetItem
    ):
        if self.settingsList.currentRow() > self.settingsArea.count():
            QtWidgets.QMessageBox.critical(self, "Error", "Settings not found")
            return
        self.settingsArea.setCurrentIndex(self.settingsList.currentRow())

    def mainSettings(self):
        generalItem = QtWidgets.QListWidgetItem("General")
        font = generalItem.font()
        font.setPointSize(14)
        font.setBold(True)
        generalItem.setFont(font)
        appearanceItem = QtWidgets.QListWidgetItem("Appearance")
        appearanceItem.setFont(font)
        audioItem = QtWidgets.QListWidgetItem("Audio")
        audioItem.setFont(font)
        return [
            generalItem,
            appearanceItem,
            audioItem,
        ]

    def add_settings(self, settings):
        for setting in settings:
            self.settingsList.addItem(setting)

    def closeEvent(self, event):
        self.write_settings()
        self.settings.sync()
        event.accept()

    def write_settings(self):
        self.settings.setValue("theme", self.theme)
        self.settings.setValue("language", self.language)
        self.settings.setValue("volume", self.volume)

    def read_settings(self):
        self.theme = self.settings.value("theme", "dark")
        self.language = self.settings.value("language", "en")
        self.volume = self.settings.value("volume", 50)


class GeneralSettings(QtWidgets.QTabWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.generalTab = GeneralTab()
        self.uiTab = UITab()
        self.addTab(self.generalTab, "General")
        self.addTab(self.uiTab, "UI")


class GeneralTab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.label = QtWidgets.QLabel("General")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
        
class UITab(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.label = QtWidgets.QLabel("UI")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)

class AppearanceSettings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.label = QtWidgets.QLabel("Appearance")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)


class AudioSettings(QtWidgets.QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.build_ui()

    def build_ui(self):
        self.label = QtWidgets.QLabel("Audio")
        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.label)
        self.setLayout(self.layout)
