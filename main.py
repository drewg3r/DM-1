from sfuncs import *
import sys
from PyQt5 import QtWidgets
import core, iface, iface2
from PyQt5.QtWidgets import *


def main():
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    window = iface.MyApp()  # Создаём объект класса ExampleApp
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


U = set(range(1, 255))


def calc_optimized(A, B, C):
    D = fintersection(A, B)
    D = fintersection(D, fadd(C, U))
    return D


# TODO: poshitat` bolshoe govno
def calc_nonoptimized(A, B, C):
    pass


def calc_optimized_totalytrue(A, B, C):
    D = A.intersection(B)
    D = D.intersection(U.difference(C))
    return D


# TODO: poshitat` bolshoe govno
def calc_nonoptimized_totalytrue(A, B, C):
    pass


global A
A = {9, 3, 5, 9}
B = {2, 4, 6, 8, 9}
C = {1, 2, 3, 15}


print(calc_optimized(A, B, C))
print(calc_optimized_totalytrue(A, B, C))

main()
