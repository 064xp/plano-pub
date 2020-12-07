from modules.funcionesAyuda import FuncionesAyuda as ayuda

class Alumno:
    def __init__(self, registro, materiasPendientes, carrera, materiasPorCuatri = 0, cuatri = 1):
        self._registro = registro
        self.materiasPendientes = materiasPendientes
        self._carrera = carrera
        self.materiasPorCuatri = 0
        self.cuatri = 1

    def __str__(self):
        return f'Alumno: {self._registro} Carrera: {self._carrera}'

    def aDict(self):
        return {
            'registro': self.registro,
            'materiasPendientes': [ayuda.normalizar(materia.nombre) for materia in self.materiasPendientes],
            'carrera': self.carrera,
            'materiasPorCuatri': self.materiasPorCuatri,
            'cuatri': self.cuatri
        }

    @staticmethod
    def buscarAlumno(registro, lista):
        for alumno in lista:
            if alumno.registro == registro:
                return alumno
        return None

    @property
    def registro(self):
        return self._registro

    @property
    def carrera(self):
        return self._carrera
