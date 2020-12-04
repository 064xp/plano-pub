from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from modules.GUI.Items import *

from modules.GUI.modulosUI.ResultadosForm import Ui_ResultadosForm

class ResultadosWindow(qtw.QMainWindow, Ui_ResultadosForm):
    def __init__(self, materias, archivo, alumnos):
        super().__init__()
        self.materias = materias
        self.alumnos = alumnos
        self.setupUi(self)
        self.setWindowTitle(f'Resultados {archivo}')
        self.show()

        modeloGrupos = self.crearModeloGrupos()
        self.GruposTreeView.setModel(modeloGrupos)
        self.GruposTreeView.setHeaderHidden(True)
        self.GruposTreeView.setAnimated(True)
        # self.GruposTreeView.setDragDropMode(qtw.QAbstractItemView.InternalMove)
        self.GruposTreeView.setAutoScroll(True)

        modeloAlumnos = self.crearModeloAlumnos()
        self.AlumnosTreeView.setModel(modeloAlumnos)
        self.AlumnosTreeView.setHeaderHidden(True)
        self.AlumnosTreeView.setAnimated(True)
        self.GruposTreeView.setAutoScroll(True)

    def crearModeloGrupos(self):
        modelo = qtg.QStandardItemModel()
        root = modelo.invisibleRootItem()
        filas = []

        for materia in self.materias.values():
            for grupo in materia.grupos:
                filas.append(GruposItem(grupo))
        root.appendRows(filas)
        return modelo

    def crearModeloAlumnos(self):
        modelo = qtg.QStandardItemModel()
        root = modelo.invisibleRootItem()
        filas = []

        for alumno in self.alumnos:
            grupos = self.gruposDeAlumno(alumno)
            filas.append(AlumnosItem(alumno, grupos))
        root.appendRows(filas)
        return modelo

    def gruposDeAlumno(self, alumno):
        grupos = []
        for materia in self.materias.values():
            for grupo in materia.grupos:
                for alumnoGrupo in grupo.alumnos:
                    if alumnoGrupo == alumno:
                        grupos.append(grupo)
        return grupos
