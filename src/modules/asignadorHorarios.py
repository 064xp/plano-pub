class AsignadorHorarios:
    def __init__ (self, materias, primeraHora, horaReceso):
        self.materias = materias
        self.primeraHora = primeraHora
        self.horaReceso = horaReceso
        self.tblHorarios = {
        'lunes' : {},
        'martes' : {},
        'miercoles' : {},
        'jueves' : {},
        'viernes' : {}
        }

    def asignar (self):
        for materia in self.materias.values():
            for grupo in materia.grupos:
                dias = self.diasSemana()
                horasPorSemana = materia.horasPorSemana
                horaSugerida = self.primeraHora
                #Si tiene lab, necesitamos saber si ya le asignamos las 2 hrs de lab
                asignoLab = False

                while horasPorSemana > 0:
                    diaStr = next(dias)
                    if not self.existeHorarioEn(diaStr,horaSugerida):
                        self.tblHorarios[diaStr][str(horaSugerida)] = []

                    while self.hayConflicto(diaStr, horaSugerida, grupo):
                        horaSugerida+=1

                    if materia.tieneLab and not asignoLab:
                        if not self.existeHorarioEn(diaStr,horaSugerida+1):
                            self.tblHorarios[diaStr][str(horaSugerida+1)] = []
                        asignoLab = True
                        self.agregarHorario(grupo, diaStr, horaSugerida)
                        self.agregarHorario(grupo, diaStr, horaSugerida +1)
                        horasPorSemana-=2
                    else:
                        self.agregarHorario(grupo, diaStr, horaSugerida)
                        horasPorSemana-=1

                    horaSugerida = self.primeraHora

    def existeHorarioEn (self, dia, hora):
        try:
            self.tblHorarios[dia][str(hora)]
            return True
        except KeyError:
            return False

    def agregarHorario (self, grupo, dia, hora):
        self.tblHorarios[dia][str(hora)].append(grupo)
        grupo.horario[dia].append(hora)

    def hayConflicto (self, diaStr, horaSugerida, grupo):
        if horaSugerida == self.horaReceso:
            return True
        if not self.existeHorarioEn(diaStr, horaSugerida):
            self.tblHorarios[diaStr][str(horaSugerida)] = []
            return False
        gruposExistentes = self.tblHorarios[diaStr][str(horaSugerida)]
        for alumno in grupo.alumnos:
            for grupoExistente in gruposExistentes:
                if alumno in grupoExistente.alumnos:
                    return True
        return False

    def diasSemana(self):
        dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes']
        actual = 0
        while True:
            if actual == 5:
                actual = 0
            yield dias[actual]
            actual += 1
