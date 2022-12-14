from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg
from modules.GUI.modulosUI.Items import *
from modules.GUI.UIBase.ResultadosForm import Ui_ResultadosForm
from modules.exportador import Exportador

class ResultadosWindow(qtw.QMainWindow, Ui_ResultadosForm):
    def __init__(self, materias, archivo, alumnos):
        super().__init__()
        self.materias = materias
        self.alumnos = alumnos
        self.archivo = archivo
        self.setupUi(self)
        self.setWindowTitle(f'Resultados {self.archivo}')
        self.show()

        self.actionExportar_Excel.triggered.connect(self.exportar)

        # Tree view Grupos
        self.modeloGrupos = self.crearModeloGrupos()
        self.modeloGrupos.setHorizontalHeaderLabels(['Grupos'])
        self.GruposTreeView.setModel(self.modeloGrupos)
        self.GruposTreeView.setAnimated(True)
        # self.GruposTreeView.setDragDropMode(qtw.QAbstractItemView.InternalMove)

        # Tree view Alumnos
        modeloAlumnos = self.crearModeloAlumnos()
        modeloAlumnos.setHorizontalHeaderLabels(['Alumnos'])
        self.AlumnosTreeView.setModel(modeloAlumnos)
        self.AlumnosTreeView.setAnimated(True)
        self.GruposTreeView.setAutoScroll(True)

        # Tree view materias
        modeloMaterias = self.crearModeloMaterias()
        modeloMaterias.setHorizontalHeaderLabels(['Materias'])
        self.materiasProxyModel = ProxyModelMaterias()
        self.materiasProxyModel.setSourceModel(modeloMaterias)
        self.MateriasTreeView.setModel(self.materiasProxyModel)
        self.MateriasTreeView.setAnimated(True)
        self.MateriasTreeView.setAutoScroll(True)

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

    def crearModeloMaterias(self):
        modelo = qtg.QStandardItemModel()
        root = modelo.invisibleRootItem()
        filas = []

        for materia in self.materias.values():
            filas.append(MateriaItem(materia))
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

    def exportar(self):
        try:
            p = re.compile(r'[\\\/]([a-zA-Z]+).xlsx', re.IGNORECASE)
            nombreDefault = p.search(self.archivo).group(1) + '_export'
        except:
            nombreDefault = 'exportHorario'

        archivoGuardar =  qtw.QFileDialog.getSaveFileName(self, 'Exportar Archivo',
            f'../{nombreDefault}', "Horario (*.xlsx)")[0]

        if not archivoGuardar:
            return

        if archivoGuardar[:5] != '.xlsx':
            archivoGuardar += '.xlsx'

        exportador = Exportador(archivoGuardar)
        exportador.exportarExcel(self.materias)
