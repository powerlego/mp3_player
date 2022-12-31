from PySide6.QtWidgets import QMainWindow
from PySide6 import QtWidgets
from PySide6 import QtCore
from PySide6 import QtGui
from .settings_window import SettingsWindow


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
        self.settings = QtCore.QSettings()
        if(self.settings.value("theme", "dark") == "dark"):
            self.setProperty("darkMode", True)
            self.menuBar().setProperty("darkMode", True)
        else:
            self.setProperty("darkMode", False)
            self.menuBar().setProperty("darkMode", False)
            
        self.read_settings()
        self.create_actions()
        self.create_menus()
        self.setMinimumSize(160, 160)
        self.resize(480, 320)
        
    def read_settings(self):
        self.theme = self.settings.value("theme", "dark")
        self.language = self.settings.value("language", "en")
        self.volume = self.settings.value("volume", 50)
        
    def write_settings(self):
        self.settings.setValue("theme", self.theme)
        self.settings.setValue("language", self.language)
        self.settings.setValue("volume", self.volume)
        
    def closeEvent(self, event):
        self.write_settings()
        self.settings.sync()
        event.accept()

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

        # ---------------------------------------------------------------------------- #
        #                                   Edit Menu                                  #
        # ---------------------------------------------------------------------------- #

        # ----------------------------------- Undo ----------------------------------- #
        self.undo_action = QtGui.QAction(self.tr("Undo"), self)
        self.undo_action.setShortcut(QtGui.QKeySequence.StandardKey.Undo)
        self.undo_action.setStatusTip(self.tr("Undo the last action"))
        self.undo_action.triggered.connect(self.undo)

        # ----------------------------------- Redo ----------------------------------- #
        self.redo_action = QtGui.QAction(self.tr("Redo"), self)
        self.redo_action.setShortcut(QtGui.QKeySequence.StandardKey.Redo)
        self.redo_action.setStatusTip(self.tr("Redo the last action"))
        self.redo_action.triggered.connect(self.redo)

        # ------------------------------------ Cut ----------------------------------- #
        self.cut_action = QtGui.QAction(self.tr("Cut"), self)
        self.cut_action.setShortcut(QtGui.QKeySequence.StandardKey.Cut)
        self.cut_action.setStatusTip(self.tr("Cut the selected item"))
        self.cut_action.triggered.connect(self.cut)

        # ----------------------------------- Copy ----------------------------------- #
        self.copy_action = QtGui.QAction(self.tr("Copy"), self)
        self.copy_action.setShortcut(QtGui.QKeySequence.StandardKey.Copy)
        self.copy_action.setStatusTip(self.tr("Copy the selected item"))
        self.copy_action.triggered.connect(self.copy)

        # ----------------------------------- Paste ---------------------------------- #
        self.paste_action = QtGui.QAction(self.tr("Paste"), self)
        self.paste_action.setShortcut(QtGui.QKeySequence.StandardKey.Paste)
        self.paste_action.setStatusTip(self.tr("Paste the item from the clipboard"))
        self.paste_action.triggered.connect(self.paste)

        # ---------------------------------- Delete ---------------------------------- #
        self.delete_action = QtGui.QAction(self.tr("Delete"), self)
        self.delete_action.setShortcut(QtGui.QKeySequence.StandardKey.Delete)
        self.delete_action.setStatusTip(self.tr("Delete the selected item"))
        self.delete_action.triggered.connect(self.delete)

        # -------------------------------- Preferences ------------------------------- #
        self.preferences_action = QtGui.QAction(self.tr("Preferences"), self)
        self.preferences_action.setShortcut(QtGui.QKeySequence.StandardKey.Preferences)
        self.preferences_action.setStatusTip(self.tr("Change the player's preferences"))
        self.preferences_action.triggered.connect(self.preferences)

        # ---------------------------------------------------------------------------- #
        #                                   Help Menu                                  #
        # ---------------------------------------------------------------------------- #

        # ----------------------------------- Help ----------------------------------- #
        self.help_action = QtGui.QAction(self.tr("Help"), self)
        self.help_action.setShortcut(QtGui.QKeySequence.StandardKey.HelpContents)
        self.help_action.setStatusTip(self.tr("Open the help file"))
        self.help_action.triggered.connect(self.help)

        # ----------------------------------- About ---------------------------------- #
        self.about_action = QtGui.QAction(self.tr("About"), self)
        self.about_action.setStatusTip(self.tr("About the application"))
        self.about_action.triggered.connect(self.about)

    def create_menus(self):
        # ---------------------------------------------------------------------------- #
        #                                   File Menu                                  #
        # ---------------------------------------------------------------------------- #
        self.file_menu = self.menuBar().addMenu(self.tr("File"))
        self.file_menu.addAction(self.new_playlist_action)
        self.file_menu.addAction(self.open_action)
        self.file_menu.addSeparator()
        # ------------------------------ Import Submenu ------------------------------ #
        self.import_menu = self.file_menu.addMenu(self.tr("Import"))
        self.import_menu.addAction(self.import_file_action)
        self.import_menu.addAction(self.import_folder_action)
        self.import_menu.addAction(self.import_playlist_action)

        self.file_menu.addAction(self.export_action)
        self.file_menu.addSeparator()
        self.file_menu.addAction(self.quit_action)

        # ---------------------------------------------------------------------------- #
        #                                   Edit Menu                                  #
        # ---------------------------------------------------------------------------- #
        self.edit_menu = self.menuBar().addMenu(self.tr("Edit"))
        self.edit_menu.addAction(self.undo_action)
        self.edit_menu.addAction(self.redo_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.cut_action)
        self.edit_menu.addAction(self.copy_action)
        self.edit_menu.addAction(self.paste_action)
        self.edit_menu.addAction(self.delete_action)
        self.edit_menu.addSeparator()
        self.edit_menu.addAction(self.preferences_action)

        # ---------------------------------------------------------------------------- #
        #                                   Help Menu                                  #
        # ---------------------------------------------------------------------------- #
        self.help_menu = self.menuBar().addMenu(self.tr("Help"))
        self.help_menu.addAction(self.help_action)
        self.help_menu.addAction(self.about_action)
        
        
        if(self.settings.value("theme") == "dark"):
            self.file_menu.setProperty("darkMode", True)
            self.import_menu.setProperty("darkMode", True)
            self.edit_menu.setProperty("darkMode", True)
            self.help_menu.setProperty("darkMode", True)
        else:
            self.file_menu.setProperty("darkMode", False)
            self.import_menu.setProperty("darkMode", False)
            self.edit_menu.setProperty("darkMode", False)
            self.help_menu.setProperty("darkMode", False)

    # ---------------------------------------------------------------------------- #
    #                           File Menu Action Methods                           #
    # ---------------------------------------------------------------------------- #
    def import_file(self):
        # TODO: Implement import file
        print("Import File")

    def import_folder(self):
        # TODO: Implement import folder
        print("Import Folder")

    def import_playlist(self):
        # TODO: Implement import playlist
        print("Import Playlist")

    def export(self):
        # TODO: Implement export
        print("Export")

    def open(self):
        # TODO: Implement open
        print("Open")

    def new_playlist(self):
        # TODO: Implement new playlist
        print("New Playlist")

    # ---------------------------------------------------------------------------- #
    #                           Edit Menu Action Methods                           #
    # ---------------------------------------------------------------------------- #
    def undo(self):
        # TODO: Implement undo
        print("Undo")

    def redo(self):
        # TODO: Implement redo
        print("Redo")

    def cut(self):
        # TODO: Implement cut
        print("Cut")

    def copy(self):
        # TODO: Implement copy
        print("Copy")

    def paste(self):
        # TODO: Implement paste
        print("Paste")

    def delete(self):
        # TODO: Implement delete
        print("Delete")

    def preferences(self):
        # TODO: Implement preferences
        settings_window = SettingsWindow()
        settings_window.exec()
        print("Preferences")

    # ---------------------------------------------------------------------------- #
    #                           Help Menu Action Methods                           #
    # ---------------------------------------------------------------------------- #
    def help(self):
        # TODO: Implement help
        print("Help")

    def about(self):
        # TODO: Implement about
        print("About")
