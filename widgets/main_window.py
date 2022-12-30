from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        widget = QtWidgets.QWidget()
        self.setCentralWidget(widget)
        label = QtWidgets.QLabel("Hello World")
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(label)
        widget.setLayout(layout)
        self.setMinimumSize(160, 160)
        self.resize(480, 320)