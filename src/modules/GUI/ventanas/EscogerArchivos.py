from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from modules.GUI.UIBase.ArchivosForm import Ui_ArchivosForm
from modules.GUI.modulosUI.DialogoAlerta import DialogoAlerta

class EscogerArchivos(qtw.QWidget, Ui_ArchivosForm):
    def __init__(self, principales, adicionales, mapas):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle('Escoger Archivos')

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

    def setDatosPrincipales(self):
        self.datosPrincipales = self.obtenerArchivo()[0]
        self.labelPrincipal.setText(self.datosPrincipales)
        if self.datosPrincipales:
            self.labelPrincipal.setVisible(True)


    def setDatosAdicionales(self):
        self.datosAdicionales = self.obtenerArchivo()[0]
        self.labelAdicional.setText(self.datosAdicionales)
        if self.datosAdicionales:
            self.labelAdicional.setVisible(True)

    def setMapas(self):
        self.mapas = self.obtenerArchivo()[0]
        self.labelMapas.setText(self.mapas)
        if self.mapas:
            self.labelMapas.setVisible(True)

    def obtenerArchivo(self):
        fileName = qtw.QFileDialog.getOpenFileName(self,
            "Abrir Archivo", "../", "Excel (*.xlsx)")
        return fileName

    def comenzar(self):
        if not (self.datosAdicionales and self.datosPrincipales and self.mapas):
            DialogoAlerta('Escoge Archivos', 'Favor de escoger los archivos')
