import sys
from PyQt5 import QtWidgets
import interface.w1, iface2, iface3, iface4, iface5
from PyQt5.QtWidgets import *
import random
import core


def showError(text):
    msg = QMessageBox()
    msg.setIcon(QMessageBox.Critical)
    msg.setText("Помилка!")
    msg.setInformativeText(text)
    msg.setWindowTitle("Помилка")
    msg.exec_()


class MyApp(QtWidgets.QMainWindow, interface.w1.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.statusBar.showMessage("Тарасенко Андрій; номер у списку: 26; ІО-91")
        self.pushButton.clicked.connect(self.var_btn)
        self.pushButton_12.clicked.connect(self.u_btn)
        self.pushButton_2.clicked.connect(self.genA_btn)
        self.pushButton_3.clicked.connect(self.genB_btn)
        self.pushButton_4.clicked.connect(self.genC_btn)
        self.pushButton_5.clicked.connect(self.setA_btn)
        self.pushButton_6.clicked.connect(self.setB_btn)
        self.pushButton_7.clicked.connect(self.setC_btn)
        self.pushButton_8.clicked.connect(self.secondW_btn)
        self.pushButton_9.clicked.connect(self.thirdW_btn)
        self.pushButton_10.clicked.connect(self.fourthW_btn)
        self.pushButton_11.clicked.connect(self.fifthW_btn)

    def var_btn(self):
        try:
            G = int(self.lineEdit.text())
            N = int(self.lineEdit_2.text()) + 2
            self.label_9.setText(str((N + G % 60) % 30 + 1))
        except:
            self.label_9.setText("??")

    def u_btn(self):
        try:
            min = int(self.lineEdit_10.text())
            max = int(self.lineEdit_11.text())
            core.U = set(range(min, max))
            print(core.U)
        except:
            showError("Некоректно введені дані")

    def genA_btn(self):
        try:
            max = int(self.lineEdit_4.text())
            s = ""
            for i in range(max):
                s = s + str(random.randint(1, 255)) + ", "
            self.lineEdit_9.setText(s[:-2])
        except:
            showError("Некоректно введені дані")

    def genB_btn(self):
        try:
            max = int(self.lineEdit_6.text())
            s = ""
            for i in range(max):
                s = s + str(random.randint(1, 255)) + ", "
            self.lineEdit_8.setText(s[:-2])
        except:
            showError("Некоректно введені дані")

    def genC_btn(self):
        try:
            max = int(self.lineEdit_5.text())
            s = ""
            for i in range(max):
                s = s + str(random.randint(1, 255)) + ", "
            self.lineEdit_7.setText(s[:-2])
        except:
            showError("Некоректно введені дані")

    def setA_btn(self):
        try:
            s = self.lineEdit_9.text().split(", ")
            for e in s:
                core.A.add(int(e))
            print("A: {}".format(core.A))
        except:
            showError("Некоректно введені дані")

    def setB_btn(self):
        try:
            s = self.lineEdit_8.text().split(", ")
            for e in s:
                core.B.add(int(e))
            print("B: {}".format(core.B))
        except:
            showError("Некоректно введені дані")

    def setC_btn(self):
        try:
            s = self.lineEdit_7.text().split(", ")
            for e in s:
                core.C.add(int(e))
            print("C: {}".format(core.C))
        except:
            showError("Некоректно введені дані")

    def secondW_btn(self):
        self.window = iface2.MyForm2()
        self.window.show()

    def thirdW_btn(self):
        self.window = iface3.MyForm3()
        self.window.show()

    def fourthW_btn(self):
        self.window = iface4.MyForm4()
        self.window.show()

    def fifthW_btn(self):
        self.window = iface5.MyForm5()
        self.window.show()
