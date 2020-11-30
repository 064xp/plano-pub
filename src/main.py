import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modules.lectorExcel import Lector
from modules.asignador import Asignador

from modules.GUI.EscogerArchivos import EscogerArchivos
from modules.GUI.Resultados import ResultadosWindow

l = Lector('../testData/datosPrincipales.xlsx', '../testData/datosAdicionales.xlsx', '../testData/mapasCurriculares.xlsx')
materias = l.extraerMaterias()
alumnos = l.extraerAlumnos(materias)
programas = l.extraerProgramas()

asignador = Asignador(alumnos, programas, materias)
asignador.crearGrupos()

def mostrarResultados():
    global ventanaResultados
    ventanaResultados = ResultadosWindow()
    ventanaEscogerArchivos.close()

app = qtw.QApplication(sys.argv)
ventanaResultados = None
ventanaEscogerArchivos = EscogerArchivos()
ventanaEscogerArchivos.btnComenzar.clicked.connect(mostrarResultados)


sys.exit(app.exec_())
