import json
from modules.definiciones.Materia import Materia
from modules.definiciones.Programa import Programa
from modules.definiciones.Alumno import Alumno
from modules.definiciones.Grupo import Grupo

class Exportador:
    def __init__(self, archivo):
        self.archivo = archivo

    def guardar(self, materias, alumnos, programas):
        export = {
            'alumnos': [alumno.aDict() for alumno in alumnos],
            'materias': {},
            'programas': {}
        }

        for materia in materias:
            export['materias'][materia] = materias[materia].aDict()

        for programa in programas:
            export['programas'][programa] = programas[programa].aDict()

        jsonExport = json.dumps(export, indent=2)
        with open(self.archivo, 'w') as f:
            f.write(jsonExport)

    def cargar(self):
        materias = {}
        alumnos = []
        programas = {}
        with open(self.archivo, 'r') as f:
            load = json.load(f)

        ## Cargar materias
        for materia in load['materias']:
            m = load['materias'][materia]
            materiaActual = Materia(
                m['nombre'], m['programas'], m['cuatri'],
                m['horasPorSemana'], m['tieneLab'], m['prerequisito'],
                )
            for grupo in m['grupos']:
                g = Grupo(grupo['alumnos'], materiaActual, grupo['id'])
                g.horario = grupo['horario']
                materiaActual.grupos.append(g)
            materias[materia] = materiaActual

        ## Cargar alumnos
        for alumno in load['alumnos']:
            alumnoActual = Alumno(
                alumno['registro'], alumno['materiasPendientes'],
                alumno['carrera'], alumno['materiasPorCuatri'],
                alumno['cuatri']
            )
            # poner referencias a las materias, no solo los ids
            materiasP = []
            for materia in alumnoActual.materiasPendientes:
                materiasP.append(materias[materia])
            alumnoActual.materiasPendientes = materiasP
            alumnos.append(alumnoActual)

        ## Poner referencias a obj alumno en grupos, no solo registro
        for materia in materias.values():
            for grupo in materia.grupos:
                alumnosRef = []
                for regAlumno in grupo.alumnos:
                    al = Alumno.buscarAlumno(regAlumno, alumnos)
                    alumnosRef.append(al)
                grupo.alumnos = alumnosRef

        ## Cargar programas
        for programa in load['programas'].values():
            programas[programa['nombre']] = Programa(programa['nombre'], programa['materiasPorCuatri'])

        return materias, alumnos, programas
