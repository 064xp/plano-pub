from PyQt5 import QtGui as qtg

class GruposItem(qtg.QStandardItem):
    def __init__(self, grupo):
        super().__init__()
        self.grupo = grupo
        self.setEditable(False)
        self.setText(f'Grupo de {self.grupo.materia}')

        for alumno in self.grupo.alumnos:
            self.appendRow(AlumnosItem(alumno))

class AlumnosItem(qtg.QStandardItem):
    def __init__(self, alumno):
        super().__init__()
        self.alumno = alumno
        self.setEditable(False)
        self.setText(f'Alumno: {self.alumno.registro}')
