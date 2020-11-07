from openpyxl import load_workbook
from modules.Materia import Materia
from modules.Programa import Programa
from modules.Alumno import Alumno

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
        for hoja in self._wbPrincipal:
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

    def extraerAlumnos(self):
        alumnos = []
        for hoja in self._wbPrincipal:
            for i, fila in enumerate(hoja.rows):
                if i in [0, 1]:
                     continue
                try:
                     registro = int(fila[0].value)
                     materiasPendientes = []
                except:
                     break

                for celda in fila:
                    if celda.column == 1:
                        continue

                    try: # si ya no hay mas materias
                        materia = self._extraerNombreMateria(hoja.cell(column = celda.column, row = 2).value)
                    except:
                        break
                    calificacion = 0

                    if celda.value is None:
                        pass
                    elif type(celda.value) == int:
                        calificacion = celda.value
                    elif celda.value.isnumeric():
                        calificacion = int(celda.value)
                    else:
                        calificacion = 0

                    if calificacion <= 5:
                        materiasPendientes.append(materia)

                alumnos.append(Alumno(registro, materiasPendientes))
        return alumnos

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
                self._extraerNombreMateria(materia)
            except:
                break

            try:
                prerequisito = prerequisitos[programa][nombreClase.upper()]
            except:
                prerequisito = None

            materias.append(Materia(nombreClase, ws.title, prerequisito))

        return materias

    def _extraerNombreMateria(self, nombre):
        paren = nombre.index('(')
        nombreClase = nombre[:paren].rstrip()
        return nombreClase
