from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modules.GUI.modulosUI.ResultadosForm import Ui_ResultadosForm

class ResultadosWindow(qtw.QMainWindow, Ui_ResultadosForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.show()
