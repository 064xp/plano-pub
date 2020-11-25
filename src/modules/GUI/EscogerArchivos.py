import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

from ArchivosForm import Ui_ArchivosForm

class MainWindow(qtw.QWidget, Ui_ArchivosForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.setupUi(self)
        self.datosPrincipales = ''
        self.datosAdicionales = ''
        self.mapas = []

        # code goes here
        self.btnDatosPrincipales.clicked.connect(self.setDatosPrincipales)
        self.btnDatosAdicionales.clicked.connect(self.setDatosAdicionales)
        self.btnMapas.clicked.connect(self.setMapas)
        self.btnComenzar.clicked.connect(self.comenzar)

        self.show()

    def setDatosPrincipales(self):
        if not self.datosPrincipales:
            self.datosPrincipales = self.obtenerArchivo()[0]
            self.crearArchivoLabelEn(self.datosPrincipales, self.ArchivosPrincipales)

    def setDatosAdicionales(self):
        if not self.datosAdicionales:
            self.datosAdicionales = self.obtenerArchivo()[0]
            self.crearArchivoLabelEn(self.datosAdicionales, self.ArchivosAdicionales)

    def setMapas(self):
        self.mapas.append(self.obtenerArchivo()[0])
        self.crearArchivoLabelEn(self.mapas[-1], self.ArchivosMapas)
        layout = self.ContVerticalLayout
        index = layout.indexOf(self.MapasWidget)
        layout.setStretch(index, 12 + len(self.mapas))

    def obtenerArchivo(self):
        fileName = qtw.QFileDialog.getOpenFileName(self,
            "Abrir Archivo", "/home/", "Excel (*.xlsx)")
        return fileName

    def crearArchivoLabelEn(self, archivo, padre):
            label = qtw.QLabel(archivo)
            label.setStyleSheet('color: white; font-size: 13px;')
            if padre.layout():
                layout = padre.layout()
                layout.addWidget(label)
            else:
                layout = qtw.QVBoxLayout()
                layout.addWidget(label)
                padre.setLayout(layout)

    def comenzar(self):
        msgBox = qtw.QMessageBox()
        msgBox.setIcon(qtw.QMessageBox.Information)
        msgBox.setWindowTitle("Comenzando...")
        msgBox.setText("Formando grupos y creando horarios...")
        msgBox.exec();


app = qtw.QApplication(sys.argv)
w = MainWindow()

sys.exit(app.exec_())
