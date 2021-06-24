from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
import re

class GruposItem(qtg.QStandardItem):
    def __init__(self, grupo):
        super().__init__()
        self.grupo = grupo
        self.setEditable(False)
        self.setText(f'{self.grupo.materia.nombre} (Grupo {self.grupo.id})   [{len(self.grupo.alumnos)} Alumnos]')
        self.tituloAlumnos = TituloItem(f'Alumnos ({len(self.grupo.alumnos)})')
        self.appendRow(self.tituloAlumnos)

        preview = [str(alumno.registro) for alumno in grupo.alumnos]
        preview = ', '.join(preview)
        self.appendColumn([TituloItem('test')])

        for alumno in self.grupo.alumnos:
            self.tituloAlumnos.appendRow(AlumnosItem(alumno, []))

        self.tituloHorarios = TituloItem('Horario')
        self.appendRow(self.tituloHorarios)
        for dia in self.grupo.horario:
            horas = [str(hr) for hr in self.grupo.horario[dia]]
            horasStr =  ', '.join(horas)
            self.tituloHorarios.appendRow(TituloItem(f'{dia.title()}:  {horasStr}'))

class AlumnosItem(qtg.QStandardItem):
    def __init__(self, alumno, grupos):
        super().__init__()
        self.alumno = alumno
        self.grupos = grupos
        self.setEditable(False)
        self.setText(f'Alumno: {self.alumno.nombre}  [{self.alumno.registro}]\t'\
        f'({self.alumno.carrera})\t'\
        f'Cuatri: {self.alumno.cuatri}\t'\
        f'Materias: {len(self.grupos)}\t')

        if len(self.grupos) > 0:
            self.tituloGrupos = TituloItem('Grupos')
            self.appendRow(self.tituloGrupos)

            for grupo in self.grupos:
                self.tituloGrupos.appendRow(GruposItem(grupo))

class MateriaItem(qtg.QStandardItem):
    def __init__(self, materia):
        super().__init__()
        self.materia = materia
        self.setEditable(False)
        self.setText(f'{self.materia.nombre} ({len(self.materia.grupos)} Grupos)')

        for grupo in self.materia.grupos:
            self.appendRow(GruposItem(grupo))

class TituloItem(qtg.QStandardItem):
    def __init__(self, titulo):
        super().__init__()
        self.setEditable(False)
        self.setText(titulo)

class ProxyModelMaterias(qtc.QSortFilterProxyModel):
    def __init__(self):
        super().__init__()
        self.sort(0, qtc.Qt.DescendingOrder)

    def lessThan(self, left, right):
        izq = self.sourceModel().data(left)
        der = self.sourceModel().data(right)
        try:
            gruposIzq = re.search(r'\(.*([0-7]).*\)', izq).group(1)
            gruposDer = re.search(r'\(.*([0-7]).*\)', der).group(1)
            return gruposIzq < gruposDer
        except:
            return izq < der
