import sys
from PyQt5 import QtWidgets
import interface.w1, core
from interface.w4 import Ui_Form4
from PyQt5.QtWidgets import *
import random


def fintersection(A, B):
    A = list(A)
    B = list(B)
    C = []
    for j in range(len(A)):
        for i in range(len(B)):
            if A[j] == B[i]:
                C.append(A[j])

    return set(C)


class MyForm4(QtWidgets.QMainWindow, interface.w4.Ui_Form4):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_4.setText(str(core.B))
        self.lineEdit_6.setText(str(core.C))
        self.pushButton.clicked.connect(self.z_btn)
        self.pushButton_2.clicked.connect(self.save_btn)

    def z_btn(self):
        self.lineEdit_7.setText(str(fintersection(core.B, core.C)))

    def save_btn(self):
        with open("results/w4.txt", "w") as f:
            f.write("Z = " + self.lineEdit_7.text())
        f.close()

        with open("results/w41.txt", "w") as f:
            f.write("Z = " + str(core.B.intersection(core.C)))
        f.close()
