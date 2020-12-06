class Materia:
    def __init__(self, nombre, id, programa, cuatri, horasPorSemana, tieneLab, prerequisito = None):
        self._nombre = nombre
        self._programas = [programa]
        self._cuatri = cuatri
        self._prerequisito = prerequisito
        self._alumnos = []
        self._grupos = []
        self._horasPorSemana = horasPorSemana
        self._tieneLab = tieneLab
        self._id = id

    def __str__(self):
        cuatri = ''
        for programa in self._cuatri:
            cuatri += f'{programa}: {self._cuatri[programa]} '
        return f'Materia: {self.nombre} | Cuatris: {cuatri} | '\
        f'tiene lab: {self._tieneLab} | grupos: {len(self._grupos)}| '\
        f'hora/semana: {self._horasPorSemana}'

    def aDict(self):
        return {
            'nombre': self.nombre,
            'programas': [programa for programa in self.programas],
            'cuatri': [(carrera, self.cuatri[carrera]) for carrera in self.cuatri],
            'prerequisito': self.prerequisito,
            'alumnos': [alumno.registro for alumno in self.alumnos],
            'grupos': [grupo.id for grupo in self.grupos],
            'horasPorSemana': self.horasPorSemana,
            'tieneLab': self.tieneLab,
            'id': self.id
        }

    @property
    def prerequisito(self):
        return self._prerequisito

    @property
    def id(self):
        return self._id

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo):
        self._nombre = nuevo

    @property
    def cuatri(self):
        return self._cuatri

    def agregarCuatri(self, programa, cuatri):
        self._cuatri[programa] = cuatri[programa]

    @property
    def programas(self):
        return self._programas

    @programas.setter
    def programas(self, nuevoValor):
        if type(nuevoValor) == list:
            self._programas = nuevoValor
        else:
            raise TypeError('Los programas de una clase deben ser una lista')

    @property
    def alumnos(self):
        return self._alumnos

    @alumnos.setter
    def alumnos(self, nuevoValor):
        if type(nuevoValor) == list:
            self._alumnos = nuevoValor
        else:
            raise TypeError('Los alumnos de una clase deben ser una lista')

    @property
    def grupos(self):
        return self._grupos

    @grupos.setter
    def grupos(self, nuevoValor):
        if type(nuevoValor) == list:
            self._grupos = nuevoValor
        else:
            raise TypeError('Los grupos de una clase deben ser una lista')

    @property
    def horasPorSemana(self):
        return self._horasPorSemana

    @property
    def tieneLab(self):
        return self._tieneLab
