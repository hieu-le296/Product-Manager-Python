import sys
import os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import sqlite3
from PIL import Image

sqlConnect = sqlite3.connect("products.db")
cur = sqlConnect.cursor()

defaultImg = 'img/store.png'

class AddMember(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Add Member")
        self.setWindowIcon(QIcon('icons/icon.ico'))
        self.setGeometry(450, 150, 350, 550)
        self.setFixedSize(self.size())
        self.UI()
        self.show()

    def UI(self):
        pass