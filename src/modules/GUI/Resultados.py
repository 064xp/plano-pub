from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from modules.GUI.Items import GruposItem

from modules.GUI.modulosUI.ResultadosForm import Ui_ResultadosForm

class ResultadosWindow(qtw.QMainWindow, Ui_ResultadosForm):
    def __init__(self, materias):
        super().__init__()
        self.materias = materias
        self.setupUi(self)
        self.setWindowTitle('Resultados Horarios')
        self.show()

        modeloGrupos = self.crearModeloGrupos()
        self.GruposTreeView.setModel(modeloGrupos)
        self.GruposTreeView.setHeaderHidden(True)

    def crearModeloGrupos(self):
        modelo = qtg.QStandardItemModel()
        root = modelo.invisibleRootItem()
        filas = []

        for materia in self.materias.values():
            for grupo in materia.grupos:
                filas.append(GruposItem(grupo))

        root.appendRows(filas)
        return modelo
