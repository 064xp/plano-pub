from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modules.GUI.UIBase.BienvenidaForm import Ui_BienvenidaForm
from modules.GUI.modulosUI.DialogoAlerta import DialogoAlerta

class Bienvenida(qtw.QWidget, Ui_BienvenidaForm):
    cargar = qtc.pyqtSignal(str)
    nuevo = qtc.pyqtSignal()

    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.BtnCargar.clicked.connect(self.escogerArchivoCargar)
        self.BtnNuevo.clicked.connect(lambda: self.nuevo.emit())
        self.nuevo.connect(lambda: self.close())
        self.show()

    def escogerArchivoCargar(self):
        archivo =  qtw.QFileDialog.getOpenFileName(self, 'Escoge el Archivo',
            '../', "Horario (*.horario)")[0]

        if archivo:
            self.cargar.emit(archivo)
