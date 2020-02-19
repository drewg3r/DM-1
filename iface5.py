import sys
from PyQt5 import QtWidgets
import interface, core
from interface.w5 import Ui_Form5
from PyQt5.QtWidgets import *


def showMsg(text, icon, title):
    msg = QMessageBox()
    msg.setIcon(icon)
    msg.setText(title)
    msg.setInformativeText(text)
    msg.setWindowTitle(title)
    msg.exec_()


class MyForm5(QtWidgets.QMainWindow, interface.w5.Ui_Form5):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.pushButton.clicked.connect(self.d1_btn)
        self.pushButton_4.clicked.connect(self.d2_btn)
        self.pushButton_5.clicked.connect(self.z1_btn)
        self.pushButton_6.clicked.connect(self.z2_btn)
        self.pushButton_3.clicked.connect(self.checkD_btn)
        self.pushButton_2.clicked.connect(self.checkZ_btn)

    def d1_btn(self):
        try:
            with open('./results/w2.txt','r') as f:
                self.lineEdit_4.setText(f.read())
        except:
            showMsg("Помилка зчитування файлу", QMessageBox.Critical, "Помилка")

    def d2_btn(self):
        try:
            with open('results/w3.txt','r') as f:
                self.lineEdit_6.setText(f.read())
        except:
            showMsg("Помилка зчитування файлу", QMessageBox.Critical, "Помилка")

    def z1_btn(self):
        try:
            with open('results/w4.txt','r') as f:
                self.lineEdit_5.setText(f.read())
        except:
            showMsg("Помилка зчитування файлу", QMessageBox.Critical, "Помилка")

    def z2_btn(self):
        try:
            with open('results/w41.txt','r') as f:
                self.lineEdit_9.setText(f.read())
        except:
            showMsg("Помилка зчитування файлу", QMessageBox.Critical, "Помилка")


    def checkD_btn(self):
        if self.lineEdit_4.text() == self.lineEdit_6.text():
            showMsg("Зчитані множини збігаються", QMessageBox.Information, "Результат")
        else:
            showMsg("Зчитані множини відрізняються", QMessageBox.Critical, "Результат")

    def checkZ_btn(self):
        if self.lineEdit_5.text() == self.lineEdit_9.text():
            showMsg("Зчитані множини збігаються", QMessageBox.Information, "Результат")
        else:
            showMsg("Зчитані множини відрізняються", QMessageBox.Critical, "Результат")
