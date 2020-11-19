from modules.definiciones.Grupo import Grupo

class Asignador:
    def __init__(self, alumnos, programas, materias, minAlumnos = 10, maxAlumnos=26):
        self.alumnos = alumnos
        self.programas = programas
        self.materias = materias
        self.minAlumnos = minAlumnos
        self.maxAlumnos = maxAlumnos


    def crearGrupos(self):
        self.asignarMaterias()
        self.crearGruposEnOrden()
        self.crearGruposFueraOrden()

    def asignarMaterias(self):
        for alumno in self.alumnos:
            materias = alumno.materiasPendientes[0:10]
            cuatri = self.promediarCuatri(materias)
            materiasPorCuatri = self.programas[alumno.carrera].materiasPorCuatri[cuatri-1]
            alumno.materiasPorCuatri = materiasPorCuatri
            materias = alumno.materiasPendientes[0:materiasPorCuatri]

            for materia in materias:
                materia.alumnos.append(alumno)

    def promediarCuatri(self, materiasPendientes):
        sumaCuatri = 0
        for materia in materiasPendientes:
            sumaCuatri+= materia.cuatri
        promedio = int(sumaCuatri/len(materiasPendientes))
        return promedio

    def crearGruposEnOrden(self):
        for llaveMateria in self.materias.keys():
            materia = self.materias[llaveMateria]
            self.crearGruposDeMateria(materia)

    def crearGruposFueraOrden(self):
        for llaveMateria in self.materias.keys():
            materia = self.materias[llaveMateria]
            materia.alumnos = []

            for alumno in self.alumnos:
                if (materia in alumno.materiasPendientes
                    and materia.prerequisito not in alumno.materiasPendientes
                    and alumno.materiasPorCuatri > 0):
                    materia.alumnos.append(alumno)
            self.crearGruposDeMateria(materia)

    def crearGruposDeMateria(self, materia):
        grupos = []
        while len(materia.alumnos) >= self.minAlumnos:
            alumnosGrupo = materia.alumnos[:self.maxAlumnos]
            materia.alumnos = materia.alumnos[self.maxAlumnos:]
            grupos.append(Grupo(alumnosGrupo, materia.nombre))
        materia.grupos.extend(grupos)
        self.quitarAlumnosAsignados(grupos, materia)

    def quitarAlumnosAsignados(self, grupos, materia):
        for grupo in grupos:
            for alumno in grupo.alumnos:
                alumno.materiasPendientes.remove(materia)
                alumno.materiasPorCuatri -= 1
