import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from PySide6 import QtCore
from widgets import MainWindow
import rc


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("MP3 Player")
    app.setApplicationName("MP3 Player")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    with open("stylesheet.qss", "r") as f:
        _style = f.read()
        app.setStyleSheet(_style)
        
    if QSettings().value("theme", "dark") == "dark":
        app.setProperty("darkMode", True)
    else:
        app.setProperty("darkMode", False)

    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
