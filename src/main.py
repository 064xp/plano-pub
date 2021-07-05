import sys
import re
from PyQt5 import QtWidgets as qtw

from modules.lectorExcel import Lector
from modules.asignadorGrupos import AsignadorGrupos
from modules.asignadorHorarios import AsignadorHorarios
from modules.exportador import Exportador

from modules.GUI.ventanas.Bienvenida import Bienvenida
from modules.GUI.ventanas.EscogerArchivos import EscogerArchivos
from modules.GUI.ventanas.Resultados import ResultadosWindow
from modules.GUI.modulosUI.DialogoAlerta import DialogoAlerta

class Main:
    def __init__(self):
        self.archivoPrincipal = '../datosPredeterminados/datosPrincipales.xlsx'
        self.archivoAdicional = '../datosPredeterminados/datosAdicionales.xlsx'
        self.mapas = '../datosPredeterminados/mapasCurriculares.xlsx'
        self.archivoGuardar = ''

        self.ventanaResultados = None
        self.ventanaEscogerArchivos = EscogerArchivos(self.archivoPrincipal, self.archivoAdicional, self.mapas)
        self.ventanaEscogerArchivos.btnComenzar.clicked.connect(self.setArchivos)

        self.ventanaBienvenida = Bienvenida()
        self.ventanaBienvenida.cargar.connect(self.cargarDeArchivo)
        self.ventanaBienvenida.nuevo.connect(lambda: self.ventanaEscogerArchivos.show())

    def comenzarAnalisis(self):
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
            self.cargarDeExcel()
            self.comenzarAnalisis()

    def mostrarResultados(self):
        self.ventanaResultados = ResultadosWindow(self.materias, self.archivoPrincipal, self.alumnos)
        self.ventanaResultados.actionGuardar.triggered.connect(lambda: self.guardar())
        self.ventanaEscogerArchivos.close()

    def guardar(self):
        # Si aun no ha guardado
        if not self.archivoGuardar:
            try:
                p = re.compile(r'[\\\/]([a-z]+).xlsx', re.IGNORECASE)
                nombreDefault = p.search(self.archivoPrincipal).group(1) + '.horario'
            except:
                nombreDefault = 'Horario.horario'

            self.archivoGuardar =  qtw.QFileDialog.getSaveFileName(self.ventanaResultados, 'Guardar Archivo',
                f'../{nombreDefault}', "Horario (*.horario)")[0]

            if not self.archivoGuardar:
                return

        exportador = Exportador(self.archivoGuardar)
        exportador.guardar(self.materias, self.alumnos, self.programas)

    def cargarDeArchivo(self, archivo):
        try:
            exportador = Exportador(archivo)
            self.materias, self.alumnos, self.programas = exportador.cargar()
            self.ventanaBienvenida.close()
            self.mostrarResultados()
        except Exception:
            DialogoAlerta('Error de Lectura', 'Ocurrió un error al intentar leer el archivo')

    def cargarDeExcel(self):
        try:
            l = Lector(self.archivoPrincipal, self.archivoAdicional, self.mapas)
            self.materias = l.extraerMaterias()
            self.alumnos = l.extraerAlumnos(self.materias)
            self.programas = l.extraerProgramas()
            l.cerrarArchivos()
        except:
            DialogoAlerta('Error de Lectura', 'Hubo un error al intentar abrir los archivos')


app = qtw.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
main.db.conn.close()
