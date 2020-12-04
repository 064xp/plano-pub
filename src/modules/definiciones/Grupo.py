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
