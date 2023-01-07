from PySide6.QtGui import QPalette, QColor


class DarkTheme(QPalette):
    def __init__(self):
        super().__init__()
        # -------------------------------- Window Text ------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.WindowText, QColor("#ffffff")
        )
        self.setBrush(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.WindowText,
            QColor("#ffffff"),
        )
        self.setBrush(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.WindowText,
            QColor("#808080"),
        )

        # ----------------------------- Button Background ---------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.Button, QColor("#424245")
        )

        # ---------------------------------- Bright ---------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.Light, QColor("#979797")
        )

        # -------------------------------- Less Bright ------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.Midlight, QColor("#5e5c5b")
        )

        # ----------------------------------- Dark ----------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.Dark, QColor("#302f2e")
        )

        # --------------------------------- Less Dark -------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.Mid, QColor("#4a4947")
        )

        # -------------------------------- Normal Text ------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.Text, QColor("#ffffff")
        )
        self.setBrush(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.Text,
            QColor("#ffffff"),
        )
        self.setBrush(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.Text,
            QColor("#808080"),
        )
        
        # -------------------------------- Bright Text ------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.BrightText, QColor("#ffffff")
        )
        
        # -------------------------------- Button Text ------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.ButtonText, QColor("#ffffff")
        )
        self.setBrush(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.ButtonText,
            QColor("#ffffff"),
        )
        self.setBrush(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.ButtonText,
            QColor("#808080"),
        )
        
        # ----------------------------- Normal Background ---------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Base, QColor("#3d3d3d"))
            
        # ---------------------------------- Window ---------------------------------- #
        self.setBrush(
            QPalette.ColorGroup.All, QPalette.ColorRole.Window, QColor("#222020")
        )
        
        # ---------------------------------- Shadow ---------------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Shadow, QColor("#e7e4e0"))
        
        # --------------------------------- Highlight -------------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Highlight, QColor("#12608a"))
        
        # ------------------------------ Highlight Text ------------------------------ #
        self.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.HighlightedText, QColor("#f9f9f9")
        )
        self.setBrush(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.HighlightedText,
            QColor("#f9f9f9"),
        )
        self.setBrush(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.HighlightedText,
            QColor("#808080"),
        )
        
        # ----------------------------------- Link ----------------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.Link, QColor("#0986d3"))
        
        # ------------------------------- Link Visited ------------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.LinkVisited, QColor("#a70b06"))
        
        # --------------------------- Alternate Background --------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.AlternateBase, QColor("#5c5b5a"))
        
        # ---------------------------- Tooltip Background ---------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.ToolTipBase, QColor("#3f3f36"))
        
        # ------------------------------- Tooltip Text ------------------------------- #
        self.setBrush(QPalette.ColorGroup.All, QPalette.ColorRole.ToolTipText, QColor("#ffffff"))
        
        # ----------------------------- Placeholder Text ----------------------------- #
        self.setBrush(
            QPalette.ColorGroup.Active, QPalette.ColorRole.PlaceholderText, QColor("#ffffff")
        )
        self.setBrush(
            QPalette.ColorGroup.Inactive,
            QPalette.ColorRole.PlaceholderText,
            QColor("#ffffff"),
        )
        self.setBrush(
            QPalette.ColorGroup.Disabled,
            QPalette.ColorRole.PlaceholderText,
            QColor("#808080"),
        )
