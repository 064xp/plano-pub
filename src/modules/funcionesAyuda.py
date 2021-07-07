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
        return nombreClase.strip()

    @staticmethod
    def normalizar(nombre):
        '''
        Quita acentos y convierte a minusculas
        '''
        if type(nombre) != str:
            return nombre

        normalizado = ''.join(c for c in unicodedata.normalize('NFD', nombre)
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

    @staticmethod
    def materiaNumeralAnterior(materia):
        prevNumerals = {
            'II': 'I',
            'III': 'II',
            'IV': 'III',
            'V': 'IV',
            'VI': 'V',
            'VII': 'VI',
            'VIII': 'VII',
            'IX': 'VIII',
            'X': 'IX',
        }
        materiaAnterior = None
        # Buscamos <nombre materia> [numeral romano]
        # Importante, espacio ente nombre y numeral
        pattern = re.compile(' ([IVX]+)$', re.I)
        search = pattern.search(materia)

        if search and search.group(1) != 'I':
            # Para matener el espacio, ej. Ingles II > Ingles I, no InglesI
            patNoSpace = re.compile('([IVX]+)$', re.I)
            numeral = search.group(1)
            start = search.start()
            materiaAnterior = patNoSpace.sub(prevNumerals[numeral.upper()], materia)

        return materiaAnterior
