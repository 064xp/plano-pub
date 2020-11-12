import unicodedata

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
        return normalizado.lower()
