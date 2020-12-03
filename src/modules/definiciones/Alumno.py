class Alumno:
    def __init__(self, registro, materiasPendientes, carrera):
        self._registro = registro
        self._materiasPendientes = materiasPendientes
        self._carrera = carrera
        self.materiasPorCuatri = 0

    def __str__(self):
        return f'Alumno: {self._registro} Carrera: {self._carrera}'

    @property
    def registro(self):
        return self._registro

    @property
    def materiasPendientes(self):
        return self._materiasPendientes

    @property
    def carrera(self):
        return self._carrera

    @property
    def cuatri(self):
        return self._cuatri
