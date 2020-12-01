import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modules.GUI.modulosUI.ArchivosForm import Ui_ArchivosForm
from modules.GUI.DialogoAlerta import DialogoAlerta

class EscogerArchivos(qtw.QWidget, Ui_ArchivosForm):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.datosPrincipales = ''
        self.datosAdicionales = ''
        self.mapas = ''

        # code goes here
        self.btnDatosPrincipales.clicked.connect(self.setDatosPrincipales)
        self.btnDatosAdicionales.clicked.connect(self.setDatosAdicionales)
        self.btnMapas.clicked.connect(self.setMapas)
        self.btnComenzar.clicked.connect(self.comenzar)

        self.show()

    def setDatosPrincipales(self):
        self.datosPrincipales = self.obtenerArchivo()[0]
        self.labelPrincipal.setText(self.datosPrincipales)

    def setDatosAdicionales(self):
        self.datosAdicionales = self.obtenerArchivo()[0]
        self.labelAdicional.setText(self.datosAdicionales)

    def setMapas(self):
        self.mapas = self.obtenerArchivo()[0]
        self.labelMapas.setText(self.mapas)

    def obtenerArchivo(self):
        fileName = qtw.QFileDialog.getOpenFileName(self,
            "Abrir Archivo", "../", "Excel (*.xlsx)")
        return fileName

    def comenzar(self):
        if not self.datosAdicionales and not self.datosPrincipales and not self.mapas:
            DialogoAlerta('Escoge Archivos', 'Favor de escoger los archivos')
