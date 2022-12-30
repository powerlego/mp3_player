from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")
        self.widget = QtWidgets.QWidget()
        self.setCentralWidget(self.widget)
        label = QtWidgets.QLabel("Hello World")
        layout = QtWidgets.QVBoxLayout()
        layout.setContentsMargins(5, 5, 5, 5)
        layout.addWidget(label)
        self.widget.setLayout(layout)
        self.create_actions()
        self.create_menus()
        self.setMinimumSize(160, 160)
        self.resize(480, 320)

    def create_actions(self):
        # ---------------------------------------------------------------------------- #
        #                                   File Menu                                  #
        # ---------------------------------------------------------------------------- #

        # ------------------------------- New Playlist ------------------------------- #
        self.new_playlist_action = QtGui.QAction(self.tr("New Playlist"), self)
        self.new_playlist_action.setShortcut(QtGui.QKeySequence.StandardKey.New)
        self.new_playlist_action.setStatusTip(self.tr("Create a new playlist"))
        self.new_playlist_action.triggered.connect(self.new_playlist)

        # ----------------------------------- Open ----------------------------------- #
        self.open_action = QtGui.QAction(self.tr("Open"), self)
        self.open_action.setShortcut(QtGui.QKeySequence.StandardKey.Open)
        self.open_action.setStatusTip(self.tr("Open a file, folder, or playlist"))
        self.open_action.triggered.connect(self.open)

        # -------------------------------- Import File ------------------------------- #
        self.import_file_action = QtGui.QAction(self.tr("Import File"), self)
        self.import_file_action.setStatusTip(
            self.tr("Import a MP3 file into the current playlist")
        )
        self.import_file_action.triggered.connect(self.import_file)

        # ------------------------------- Import Folder ------------------------------ #
        self.import_folder_action = QtGui.QAction(self.tr("Import Folder"), self)
        self.import_folder_action.setStatusTip(
            self.tr("Import a folder of MP3 files into the player")
        )
        self.import_folder_action.triggered.connect(self.import_folder)

        # ------------------------------ Import Playlist ----------------------------- #
        self.import_playlist_action = QtGui.QAction(self.tr("Import Playlist"), self)
        self.import_playlist_action.setStatusTip(
            self.tr("Import a playlist into the player")
        )
        self.import_playlist_action.triggered.connect(self.import_playlist)

        # ---------------------------------- Export ---------------------------------- #
        self.export_action = QtGui.QAction(self.tr("Export"), self)
        self.export_action.setShortcut(
            QtCore.QKeyCombination(
                QtCore.Qt.KeyboardModifier.ControlModifier, QtCore.Qt.Key_E
            )
        )
        self.export_action.setStatusTip(self.tr("Export the current playlist"))
        self.export_action.triggered.connect(self.export)

        # ----------------------------------- Quit ----------------------------------- #
        self.quit_action = QtGui.QAction(self.tr("Quit"), self)
        self.quit_action.setShortcut(
            QtCore.QKeyCombination(
                QtCore.Qt.KeyboardModifier.ControlModifier, QtCore.Qt.Key_Q
            )
        )
        self.quit_action.setStatusTip("Quit the application")
        self.quit_action.triggered.connect(self.close)

    def import_file(self):
        print("Import File")

    def import_folder(self):
        print("Import Folder")

    def import_playlist(self):
        print("Import Playlist")

    def export(self):
        print("Export")

    def open(self):
        print("Open")

    def new_playlist(self):
        print("New Playlist")

    def create_menus(self):
        self.file_menu = self.menuBar().addMenu(self.tr("File"))
        self.file_menu.addAction(self.new_playlist_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addSeparator()
        self.import_menu = self.file_menu.addMenu(self.tr("Import"))
        self.import_menu.addAction(self.import_file_action)
        self.import_menu.addAction(self.import_folder_action)
        self.import_menu.addAction(self.import_playlist_action)
        self.file_menu.addAction(self.export_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.quit_action)
