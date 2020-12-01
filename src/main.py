import sys
from PyQt5 import QtWidgets as qtw

from modules.lectorExcel import Lector
from modules.asignador import Asignador

from modules.GUI.EscogerArchivos import EscogerArchivos
from modules.GUI.Resultados import ResultadosWindow

class Main:
    def __init__(self):
        self.ventanaResultados = None
        self.ventanaEscogerArchivos = EscogerArchivos()
        self.ventanaEscogerArchivos.btnComenzar.clicked.connect(self.comenzarAnalisis)
        self.archivoPrincipal = '../testData/datosPrincipales.xlsx'
        self.archivoAdicional = '../testData/datosAdicionales.xlsx'
        self.mapas = '../testData/mapasCurriculares.xlsx'

    def comenzarAnalisis(self):
        l = Lector(self.archivoPrincipal, self.archivoAdicional, self.mapas)
        self.materias = l.extraerMaterias()
        self.alumnos = l.extraerAlumnos(self.materias)
        self.programas = l.extraerProgramas()
        l.cerrarArchivos()

        asignador = Asignador(self.alumnos, self.programas, self.materias)
        asignador.crearGrupos()

        self.mostrarResultados()

    def mostrarResultados(self):
        self.ventanaResultados = ResultadosWindow()
        self.ventanaEscogerArchivos.close()

app = qtw.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
