from openpyxl import load_workbook
from modules.Materia import Materia
from modules.Programa import Programa

class Lector:
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

    def extraerMaterias(self):
        materias = []
        for sheet in self._wbPrincipal:
            ws = self._wbPrincipal[sheet.title]
            materiasPrograma = self._extraerMateriasWS(sheet.title, self._prerequisitos)

            # Checar si hay materias duplicadas
            # Si si hay, nos quedamos con la original y le agregamos el programa nuevo
            # a la lista de programas
            for materia in materias:
                for materiaP in materiasPrograma[:]:
                    if materiaP.nombre.upper() == materia.nombre.upper():
                        materia.programas.extend(materiaP.programas)
                        materiasPrograma.remove(materiaP)
            materias.extend(materiasPrograma)

        return materias

    def extraerProgramas(self):
        programas = {}
        for hoja in self._wbPrincipal:
            programa = hoja.title
            programas[programa] = Programa(programa, self.extraerCantidadMaterias(programa))
        return programas

    def _materiaExisteEn(self, materia, listaMaterias):
        for i, materiaL in enumerate(listaMaterias):
            if materia.nombre == materiaL.nombre:
                return i
        return None

    def _extraerMateriasWS(self, programa, prerequisitos):
        materias = []
        try:
            ws = self._wbPrincipal[programa]
        except:
            print(f'Error cargando hoja {programa}')
            sys.exit(1)

        for celda in tuple(ws.rows)[1]:
            if celda.column == 1:
                continue

            materia = celda.value
            try:
                paren = materia.index('(')
                nombreClase = materia[:paren].rstrip()
            except:
                break

            try:
                prerequisito = prerequisitos[programa][nombreClase.upper()]
            except:
                prerequisito = None

            materias.append(Materia(nombreClase, ws.title, prerequisito))

        return materias
