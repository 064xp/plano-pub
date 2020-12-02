import sys
from PyQt5 import QtWidgets as qtw

from modules.lectorExcel import Lector
from modules.asignadorGrupos import AsignadorGrupos
from modules.asignadorHorarios import AsignadorHorarios

from modules.GUI.EscogerArchivos import EscogerArchivos
from modules.GUI.Resultados import ResultadosWindow
from modules.GUI.DialogoAlerta import DialogoAlerta

class Main:
    def __init__(self):
        # self.archivoPrincipal = '../testData/datosPrincipales.xlsx'
        self.archivoPrincipal = ''
        self.archivoAdicional = '../testData/datosAdicionales.xlsx'
        self.mapas = '../testData/mapasCurriculares.xlsx'
        self.ventanaResultados = None
        self.ventanaEscogerArchivos = EscogerArchivos(self.archivoPrincipal, self.archivoAdicional, self.mapas)
        self.ventanaEscogerArchivos.btnComenzar.clicked.connect(self.setArchivos)

    def comenzarAnalisis(self):
        try:
            l = Lector(self.archivoPrincipal, self.archivoAdicional, self.mapas)
        except:
            DialogoAlerta('Error de Lectura', 'Hubo un error al intentar abrir los archivos')

        self.materias = l.extraerMaterias()
        self.alumnos = l.extraerAlumnos(self.materias)
        self.programas = l.extraerProgramas()
        l.cerrarArchivos()

        asignadorG = AsignadorGrupos(self.alumnos, self.programas, self.materias)
        asignadorG.crearGrupos()

        asignadorH = AsignadorHorarios(self.materias, 7, 10)
        asignadorH.asignar()

        self.mostrarResultados()

    def setArchivos(self):
        principales = self.ventanaEscogerArchivos.datosPrincipales
        adicionales =  self.ventanaEscogerArchivos.datosAdicionales
        mapas =  self.ventanaEscogerArchivos.mapas
        if principales and adicionales and mapas:
            self.archivoPrincipal = principales
            self.archivoAdicional = adicionales
            self.mapas = mapas
            self.comenzarAnalisis()

    def mostrarResultados(self):
        self.ventanaResultados = ResultadosWindow()
        self.ventanaEscogerArchivos.close()

app = qtw.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
