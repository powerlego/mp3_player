import sys
from PySide6 import QtWidgets
from PySide6.QtWidgets import QApplication, QMainWindow


def main():
    app = QApplication(sys.argv)
    window = QMainWindow()
    window.show()
    app.exec()


if __name__ == "__main__":
    main()
