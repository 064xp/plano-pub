from PyQt5 import QtWidgets as qtw
from PyQt5 import QtCore as qtc
from PyQt5 import QtGui as qtg

class DialogoAlerta(qtw.QWidget):
    def __init__(self, titulo, mensaje):
        super().__init__()
        self.titulo = titulo
        self.mensaje = mensaje
        self.initUI()
        self.show()

    def initUI(self):
        self.msgBox = qtw.QMessageBox()
        self.msgBox.setIcon(qtw.QMessageBox.Warning)
        self.msgBox.setWindowTitle(self.titulo)
        self.msgBox.setText(self.mensaje)
        self.msgBox.exec();
