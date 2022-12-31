import json
import re
from PySide6.QtCore import QFile


class ColorParser:
    def __init__(self):
        file = QFile(":/dark.json")
        file.open(QFile.ReadOnly | QFile.Text)
        jsonStr = str(file.readAll(), encoding="utf-8")
        self.darkColors = json.loads(jsonStr)
        file.close()
        file = QFile(":/light.json")
        file.open(QFile.ReadOnly | QFile.Text)
        jsonStr = str(file.readAll(), encoding="utf-8")
        self.lightColors = json.loads(jsonStr)
        file.close()
        file = QFile(":/style.qss")
        file.open(QFile.ReadOnly | QFile.Text)
        self.style = str(file.readAll(), encoding="utf-8")
        file.close()

    def parse(self, mode="dark"):
        if mode == "dark":
            for key, value in self.darkColors.items():
                self.style = re.sub(r'@%s;' % str(key), str(value)+";", self.style, flags=re.IGNORECASE | re.MULTILINE | re.DOTALL)
        else:
            for key, value in self.lightColors.items():
                self.style = re.sub(r"@\b%s\b" % str(key), str(value), self.style)
                
        return self.style
