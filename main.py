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


main()
