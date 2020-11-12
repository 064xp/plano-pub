class Materia:
    def __init__(self, nombre, programa, cuatri, prerequisito = None):
        self._nombre = nombre
        self._programas = [programa]
        self._cuatri = cuatri
        self._prerequisito = prerequisito

    @property
    def prerequisito(self):
        return self._prerequisito

    @property
    def nombre(self):
        return self._nombre

    @property
    def cuatri(self):
        return self._cuatri

    @property
    def programas(self):
        return self._programas

    @programas.setter
    def programas(self, nuevoValor):
        if type(nuevoValor) == list:
            self._programas = nuevoValor
        else:
            raise TypeError('Los programas de una clase deben ser una lista')
