from sfuncs import *
import sys
from PyQt5 import QtWidgets
import core, iface, iface2
from PyQt5.QtWidgets import *


app = QtWidgets.QApplication(sys.argv)
window = iface.MyApp()
window.show()
app.exec_()
