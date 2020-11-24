from openpyxl import load_workbook
from modules.definiciones.Materia import Materia
from modules.definiciones.Programa import Programa
from modules.definiciones.Alumno import Alumno
from modules.funcionesAyuda import FuncionesAyuda as ayuda
import sys

class Lector:
    def __init__(self, archivoPrincipal, archivoAdicionales, mapasCurriculares):
        self._wbPrincipal = load_workbook(filename=archivoPrincipal)
        self._wbAdicional = load_workbook(filename=archivoAdicionales)
        self._mapas = self.cargarMapasCurriculares(mapasCurriculares)
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

    def cargarMapasCurriculares(self, doc):
        mapas = {}
        try:
            wb = load_workbook(filename = doc)
        except:
            print('No se pudo abrir el archivo de mapas mapas curriculares')
            sys.exit(1)

        for hoja in wb:
            programa = hoja.title
            materias = {}

            for columna in hoja.columns:
                cuatri = 0
                for celda in columna:
                    if celda.row == 1:
                        cuatri = celda.value
                        continue
                    elif celda.value is None:
                        break
                    materias[ayuda.normalizar(celda.value)] = cuatri
            mapas[programa] = materias
        return mapas

    def extraerMaterias(self):
        '''
        Extrae materias de todas las hojas en el documento
        Regresa un diccionario, siendo las llaves los nombres de la materia normalizados
            (sin acentos y en minusculas)
        y los valores objetos tipo Materia
        '''
        materias = {}
        for hoja in self._wbPrincipal:
            ws = self._wbPrincipal[hoja.title]
            materiasPrograma = self._extraerMateriasWS(hoja.title, self._prerequisitos)

            # Checar si hay materias duplicadas
            # Si si hay, nos quedamos con la original y le agregamos el programa nuevo
            # a la lista de programas
            for materiaP in dict(materiasPrograma).keys():
                if materiaP in materias:
                    materias[materiaP].programas.extend(materiasPrograma[materiaP].programas)
                    materiasPrograma.pop(materiaP)
            materias.update(materiasPrograma)
        return materias

    def extraerProgramas(self):
        programas = {}
        for hoja in self._wbPrincipal:
            programa = hoja.title
            programas[programa] = Programa(programa, self.extraerCantidadMaterias(programa))
        return programas

    def extraerAlumnos(self, materias):
        '''Extrae alumnos de todas las hojas de calculo.
        Recibe un diccionario de objetos Materia (previamente extraídos)
        Un alumno tiene no. registro, carrera y materias pendientes,
        materiasPendientes es una lista de referencias a materias del diccionario
        '''
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
                        nombreMateria = ayuda.extraerNombreMateria(hoja.cell(column = celda.column, row = 2).value)
                        materia = materias[ayuda.normalizar(nombreMateria)]
                    except:
                        break
                    calificacion = 0

                    if celda.value is None:
                        pass
                    elif type(celda.value) == int:
                        calificacion = celda.value
                    elif celda.value.isnumeric():
                        calificacion = int(celda.value)
                    elif celda.value == 'NI':
                        calificacion = 10
                    else:
                        calificacion = 0

                    if calificacion <= 5:
                        materiasPendientes.append(materia)

                alumnos.append(Alumno(registro, materiasPendientes, hoja.title))
        return alumnos

    def _extraerMateriasWS(self, programa, prerequisitos):
        '''
        Extrae las materias de una hoja de Calculo
        Regresa un diccionario, las claves siendo el nombre de la materia
        los valores siendo objetos tipo Materia
        '''
        materias = {}
        try:
            ws = self._wbPrincipal[programa]
        except:
            print(f'Error cargando hoja {programa}')
            sys.exit(1)

        for celda in tuple(ws.rows)[1]:
            if celda.column == 1:
                continue

            materia = celda.value
            try: #llave del diccionario es el nombre de la materia normalizado
                nombreMateria = ayuda.extraerNombreMateria(materia)
            except:
                break

            try:
                prerequisito = prerequisitos[programa][nombreClase.upper()]
            except:
                prerequisito = None

            try:
                cuatri = self._mapas[programa][ayuda.normalizar(nombreMateria)]
            except:
                cuatri = 1
                print(f'[!] No se pudo encontrar {programa}-{nombreMateria} en mapas curriculares')

            materias[ayuda.normalizar(nombreMateria)] = Materia(nombreMateria, ws.title, cuatri, prerequisito)

        return materias
