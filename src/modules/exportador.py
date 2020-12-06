import json

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
