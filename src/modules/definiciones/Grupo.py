class Grupo:
    def __init__(self, alumnos, materia):
        self.alumnos = alumnos
        self.materia = materia
        self.horario = {
            'lunes' : [],
            'martes' : [],
            'miercoles' : [],
            'jueves' : [],
            'viernes' : []
        }
