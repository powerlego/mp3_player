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
    file = QtCore.QFile(":/style.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stylesheet = str(file.readAll(), encoding="utf-8")
    file.close()
    if QSettings().value("theme", "dark") == "dark":
        app.setProperty("darkMode", True)
    else:
        app.setProperty("darkMode", False)

    window = MainWindow()
    window.show()
    app.setStyleSheet(stylesheet)
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
