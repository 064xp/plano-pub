class Grupo:
    def __init__(self, alumnos, materia, id):
        self.alumnos = alumnos
        self.materia = materia
        self.id = id
        self.horario = {
            'lunes' : [],
            'martes' : [],
            'miercoles' : [],
            'jueves' : [],
            'viernes' : []
        }

    def __str__(self):
        return str(self.horario)

    def aDict(self):
        return {
            'alumnos': [alumno.registro for alumno in self.alumnos],
            'materia': self.materia.id,
            'id': self.id,
            'horario': self.horario
        }
