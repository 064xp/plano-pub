class Alumno:
    def __init__(self, registro, materiasPendientes, carrera, nombre = ''):
        self._registro = registro
        self._materiasPendientes = materiasPendientes
        self._carrera = carrera

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
