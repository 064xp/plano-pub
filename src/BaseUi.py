import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modulosUI.EscogerArchivos import EscogerArchivos
from modulosUI.Resultados import ResultadosWindow

a = None

def change():
    global a
    a = ResultadosWindow()
    w.close()

app = qtw.QApplication(sys.argv)
w= EscogerArchivos()
w.btnComenzar.clicked.connect(change)


sys.exit(app.exec_())
