import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modules.GUI.modulosUI.ArchivosForm import Ui_ArchivosForm
from modules.GUI.DialogoAlerta import DialogoAlerta

class EscogerArchivos(qtw.QWidget, Ui_ArchivosForm):
    def __init__(self, principales, adicionales, mapas):
        super().__init__()
        self.setupUi(self)
        self.datosPrincipales = principales
        self.datosAdicionales = adicionales
        self.mapas = mapas

        # conexiones con signals
        self.btnDatosPrincipales.clicked.connect(self.setDatosPrincipales)
        self.btnDatosAdicionales.clicked.connect(self.setDatosAdicionales)
        self.btnMapas.clicked.connect(self.setMapas)
        self.btnComenzar.clicked.connect(self.comenzar)

        self.labelPrincipal.setText(self.datosPrincipales)
        self.labelAdicional.setText(self.datosAdicionales)
        self.labelMapas.setText(self.mapas)

        if not self.datosPrincipales:
            self.labelPrincipal.setVisible(False)
        if not self.datosAdicionales:
            self.labelAdicional.setVisible(False)
        if not self.mapas:
            self.labelMapas.setVisible(False)

        self.show()

    def setDatosPrincipales(self):
        self.labelPrincipal.setVisible(True)
        self.datosPrincipales = self.obtenerArchivo()[0]
        self.labelPrincipal.setText(self.datosPrincipales)

    def setDatosAdicionales(self):
        self.labelAdicional.setVisible(True)
        self.datosAdicionales = self.obtenerArchivo()[0]
        self.labelAdicional.setText(self.datosAdicionales)

    def setMapas(self):
        self.labelMapas.setVisible(False)
        self.mapas = self.obtenerArchivo()[0]
        self.labelMapas.setText(self.mapas)

    def obtenerArchivo(self):
        fileName = qtw.QFileDialog.getOpenFileName(self,
            "Abrir Archivo", "../", "Excel (*.xlsx)")
        return fileName

    def comenzar(self):
        if not (self.datosAdicionales and self.datosPrincipales and self.mapas):
            DialogoAlerta('Escoge Archivos', 'Favor de escoger los archivos')
