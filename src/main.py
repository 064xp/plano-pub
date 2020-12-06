import sys
import re
from PyQt5 import QtWidgets as qtw

from modules.lectorExcel import Lector
from modules.asignadorGrupos import AsignadorGrupos
from modules.asignadorHorarios import AsignadorHorarios
from modules.baseDatos import BaseDatos

from modules.GUI.ventanas.EscogerArchivos import EscogerArchivos
from modules.GUI.ventanas.Resultados import ResultadosWindow
from modules.GUI.modulosUI.DialogoAlerta import DialogoAlerta

class Main:
    def __init__(self):
        self.archivoPrincipal = '../datosPredeterminados/datosPrincipales.xlsx'
        self.archivoAdicional = '../datosPredeterminados/datosAdicionales.xlsx'
        self.mapas = '../datosPredeterminados/mapasCurriculares.xlsx'
        self.dbFile = ''
        self.db = None
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
        self.ventanaResultados = ResultadosWindow(self.materias, self.archivoPrincipal, self.alumnos)
        self.ventanaResultados.actionGuardar.triggered.connect(lambda: self.guardar())
        self.ventanaEscogerArchivos.close()

    def guardar(self):
        # Si aun no ha guardado
        if not self.dbFile:
            try:
                p = re.compile(r'[\\\/]([a-z]+).xlsx', re.IGNORECASE)
                nombreDefault = p.search(self.archivoPrincipal).group(1) + '.hr'
            except:
                nombreDefault = 'Horario.hr'

            self.dbFile =  qtw.QFileDialog.getSaveFileName(self.ventanaResultados, 'Guardar Archivo',
                f'../{nombreDefault}', "Horario (*.hr)")[0]

            try:
                self.db = BaseDatos(self.dbFile)
            except:
                DialogoAlerta('Error al Guardar', 'No se pudo crear el archivo')
                return

        for materia in self.materias.values():
            self.db.insertarMateria(materia, self.materias)
            for grupo in materia.grupos:
                self.db.insertarGrupo(grupo)

        for alumno in self.alumnos:
            self.db.insertarAlumno(alumno)

app = qtw.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
main.db.conn.close()
