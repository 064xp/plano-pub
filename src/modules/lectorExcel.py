from openpyxl import load_workbook

class Lector:
    _wbPrincipal = None
    _wbAdicional = None
    def __init__(self, archivoPrincipal, archivoAdicionales):
        self._wbPrincipal = load_workbook(filename=archivoPrincipal)
        self._wbAdicional = load_workbook(filename=archivoAdicionales)
        self._prerequisitos = self.extraerPrerequisitos()

    def extraerPrerequisitos(self):
        prerequisitos = {}
        try:
            ws = self._wbAdicional['Prerequisitos']
        except:
            print('Hoja con prerequisitos de materias no encontrado')
            sys.exit(1)

        for celda in tuple(ws.columns)[0]:
            if celda.row != 1:
                programa = ws.cell(column = 1, row = celda.row).value
                materia = ws.cell(column = 2, row = celda.row).value
                prerequisito = ws.cell(column = 3, row = celda.row).value

                if not programa in prerequisitos:
                    prerequisitos[programa] = {}

                prerequisitos[programa][materia.upper()] = prerequisito
        return prerequisitos

    def extraerCantidadMaterias(self, programa):
        cantMaterias = []
        try:
            ws = self._wbAdicional['MateriasPorCuatri']
        except:
            print('Hoja con cantidad de materias por cuatri no encontrado')
            sys.exit(1)

        for celda in tuple(ws.columns)[0]:
            if celda.value == programa:
                cuatri = int(ws.cell(column = celda.column+1, row = celda.row).value)
                materias = int(ws.cell(column = celda.column+2, row = celda.row).value)
                cantMaterias.insert(cuatri, materias)
        return cantMaterias
