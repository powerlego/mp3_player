import json
from PySide6.QtCore import QFile

class ColorParser:
    def __init__(self):
        file = QFile(":/dark")
        
        self.darkColors = {}
    
    def parse(self, mode='dark'):
