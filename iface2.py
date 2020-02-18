import sys
from PyQt5 import QtWidgets
import interface.w1, core
from interface.w2 import Ui_Form2
from PyQt5.QtWidgets import *
import random


class MyForm2(QtWidgets.QMainWindow, interface.w2.Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global A
        self.lineEdit_4.setText(str(core.A))
        # pushButton pushButton_2
