# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'w2.ui'
#
# Created by: PyQt5 UI code generator 5.12.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form2(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 280)
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(150, 10, 67, 17))
        self.label.setObjectName("label")
        self.label_5 = QtWidgets.QLabel(Form)
        self.label_5.setGeometry(QtCore.QRect(20, 50, 16, 21))
        self.label_5.setObjectName("label_5")
        self.label_4 = QtWidgets.QLabel(Form)
        self.label_4.setGeometry(QtCore.QRect(20, 80, 16, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(Form)
        self.lineEdit_5.setGeometry(QtCore.QRect(40, 110, 331, 25))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(Form)
        self.lineEdit_6.setGeometry(QtCore.QRect(40, 80, 331, 25))
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.label_6 = QtWidgets.QLabel(Form)
        self.label_6.setGeometry(QtCore.QRect(20, 110, 16, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_4 = QtWidgets.QLineEdit(Form)
        self.lineEdit_4.setGeometry(QtCore.QRect(40, 50, 331, 25))
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 140, 351, 25))
        self.pushButton.setObjectName("pushButton")
        self.label_7 = QtWidgets.QLabel(Form)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 16, 21))
        self.label_7.setObjectName("label_7")
        self.lineEdit_7 = QtWidgets.QLineEdit(Form)
        self.lineEdit_7.setGeometry(QtCore.QRect(40, 180, 331, 25))
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.label_8 = QtWidgets.QLabel(Form)
        self.label_8.setGeometry(QtCore.QRect(20, 210, 71, 21))
        self.label_8.setObjectName("label_8")
        self.lineEdit_8 = QtWidgets.QLineEdit(Form)
        self.lineEdit_8.setGeometry(QtCore.QRect(90, 210, 281, 25))
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.pushButton_2 = QtWidgets.QPushButton(Form)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 240, 351, 25))
        self.pushButton_2.setObjectName("pushButton_2")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Вікно 2"))
        self.label.setText(_translate("Form", "formula"))
        self.label_5.setText(_translate("Form", "A"))
        self.label_4.setText(_translate("Form", "B"))
        self.label_6.setText(_translate("Form", "C"))
        self.pushButton.setText(_translate("Form", "Крок"))
        self.label_7.setText(_translate("Form", "D"))
        self.label_8.setText(_translate("Form", "Операція"))
        self.pushButton_2.setText(_translate("Form", "Зберегти"))
