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
