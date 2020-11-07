class Alumno:
    def __init__(self, registro, materiasPendientes, carrera, cuatri = 0, nombre = ''):
        self._registro = registro
        self._materiasPendientes = materiasPendientes
        self._carrera = carrera
        self._cuatri = cuatri
        self._nombre = nombre

    @property
    def nombre(self):
        return self._nombre

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
