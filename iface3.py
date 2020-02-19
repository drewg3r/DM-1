import sys
from PyQt5 import QtWidgets
import interface, core
from interface.w3 import Ui_Form3

# D = A ⋂ B ⋂ !C
def calcgen():
    for i in list(range(3)):
        if i == 0:
            R1 = set()
            R1 = core.A.intersection(core.B)
            yield "{} ⋂ !C".format(R1), "A ⋂ B| {}".format(R1)
        if i == 1:
            R2 = set()
            R2 = core.U - core.C
            yield "{} ⋂ {}".format(R1, R2), "!C | {}".format(R2)
        if i == 2:
            R3 = set()
            R3 = R1.intersection(R2)
            yield "{}".format(R3), "R1 ⋂ R2 | {}".format(R3)


class MyForm3(QtWidgets.QMainWindow, interface.w3.Ui_Form3):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.lineEdit_4.setText(str(core.A))
        self.lineEdit_6.setText(str(core.B))
        self.lineEdit_5.setText(str(core.C))
        self.pushButton.clicked.connect(self.calc_btn)
        self.pushButton_2.clicked.connect(self.save_btn)
        self.g = calcgen()
        # pushButton pushButton_2

    def calc_btn(self):
        try:
            r = next(self.g)
            self.lineEdit_7.setText(r[0])
            self.lineEdit_8.setText(r[1])
        except:
            pass

    def save_btn(self):
        with open("results/w3.txt", "w") as f:
            f.write("D = " + self.lineEdit_7.text())
        f.close()
