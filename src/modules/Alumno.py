class Alumno:
    def __init__(self, registro, materiasPendientes, nombre = ''):
        self._nombre = nombre
        self._registro = registro
        self._materiasPendientes = materiasPendientes

    @property
    def nombre(self):
        return self._nombre

    @property
    def registro(self):
        return self._registro

    @property
    def materiasPendientes(self):
        return self._materiasPendientes
