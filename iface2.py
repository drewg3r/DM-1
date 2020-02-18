import sys
from PyQt5 import QtWidgets
import interface.w1, core
from interface.w2 import Ui_Form2
from PyQt5.QtWidgets import *
import random

# D = !C ⋂ (A \ C) ⋂ (B \ C) ⋂ (!C ∪ B)
def calcgen():
    for i in list(range(6)):
        if i == 0:
            R1 = set()
            R1 = core.A - core.C
            yield "!C ⋂ {} ⋂ (B \ C) ⋂ (!C ∪ B)".format(R1), "A \ C | {}".format(R1)
        if i == 1:
            R2 = set()
            R2 = core.B - core.C
            yield "!C ⋂ {} ⋂ {} ⋂ (!C ∪ B)".format(R1, R2), "B \ C | {}".format(R2)
        if i == 2:
            R3 = set()
            R3 = (core.U - core.C).union(core.B)
            yield "!C ⋂ {} ⋂ {} ⋂ {}".format(R1, R2, R3), "!C ∪ B | {}".format(R3)
        if i == 3:
            R4 = set()
            R4 = (core.U - core.C).intersection(R1)
            yield "{} ⋂ {} ⋂ {}".format(R4, R2, R3), "!C ⋂ R1 | {}".format(R4)
        if i == 4:
            # R5 = set()
            R5 = R4.intersection(R2)
            yield "{} ⋂ {}".format(R5, R3), "R4 ⋂ R2 | {}".format(R5)
        if i == 5:
            R6 = set()
            R6 = R5.intersection(R3)
            yield "{}".format(R6), "R5 ⋂ R3 | {}".format(R6)


class MyForm2(QtWidgets.QMainWindow, interface.w2.Ui_Form2):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        global A
        self.lineEdit_4.setText(str(core.A))
        self.lineEdit_6.setText(str(core.B))
        self.lineEdit_5.setText(str(core.C))
        self.pushButton.clicked.connect(self.calc_btn)
        self.g = calcgen()
        # pushButton pushButton_2

    def calc_btn(self):
        try:
            r = next(self.g)
            self.lineEdit_7.setText(r[0])
            self.lineEdit_8.setText(r[1])
        except:
            pass
