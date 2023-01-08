import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication
from PySide6.QtCore import QSettings
from PySide6 import QtCore
from widgets import MainWindow
from utils import DarkTheme
import rc



def main():
    app = QApplication(sys.argv)
    app.setOrganizationName("MP3 Player")
    app.setApplicationName("MP3 Player")
    QSettings.setDefaultFormat(QSettings.IniFormat)
    app.setStyle(QtWidgets.QStyleFactory.create("fusion"))
    
    file = QtCore.QFile(":/style.qss")
    file.open(QtCore.QFile.ReadOnly | QtCore.QFile.Text)
    stylesheet = file.readAll().toStdString()
    file.close()
    app.setStyleSheet(stylesheet)
    if(QSettings().value("theme", "dark") == "dark"):
        app.setPalette(DarkTheme())
        
    # stylesheet = ColorParser().parse(QSettings().value("theme", "dark"))
    # app.setStyleSheet(stylesheet)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


if __name__ == "__main__":
    main()
