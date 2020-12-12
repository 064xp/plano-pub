import unicodedata
import re

class FuncionesAyuda:
    @staticmethod
    def extraerNombreMateria(nombre):
        '''
        Extrae el nombre de la materia de una cadena
        del formato <materia> ([codigoMateria])
        ej. Algebra II (12345) => Algebra II
        '''
        paren = nombre.index('(')
        nombreClase = nombre[:paren].rstrip()
        return nombreClase

    @staticmethod
    def normalizar(str):
        '''
        Quita acentos y convierte a minusculas
        '''
        normalizado = ''.join(c for c in unicodedata.normalize('NFD', str)
                            if unicodedata.category(c) != 'Mn')
        return normalizado.lower().replace(' ', '')

    @staticmethod
    def extraerCarreraPlan(nombres):
        carreras = []
        planes = []

        for nombre in nombres:
            search = re.search(r'([a-zA-Z]+).([0-9]+)', nombre)
            carreras.append(search.group(1))
            planes.append(search.group(2)[-2:])

        carrerasStr = ', '.join(carreras)
        planesStr = ', '.join(planes)
        return carrerasStr, planesStr
