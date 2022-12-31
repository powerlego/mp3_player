import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from widgets import MainWindow


def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("MP3 Player")
    app.setApplicationName("MP3 Player")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
