class Programa:
    def __init__(self, nombre, materiasPorCuatri):
        self.nombre = nombre
        self.materiasPorCuatri = materiasPorCuatri

    def aDict(self):
        return {
            'nombre': self.nombre,
            'materiasPorCuatri': self.materiasPorCuatri
        }
