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
            cuatri = self.calcularCuatri(materias)
            materiasPorCuatri = self.programas[alumno.carrera].materiasPorCuatri[cuatri-1]
            alumno.materiasPorCuatri = materiasPorCuatri
            materias = alumno.materiasPendientes[0:materiasPorCuatri]

            for materia in materias:
                materia.alumnos.append(alumno)

    def calcularCuatri(self, materiasPendientes):
        cantidad = []
        cuatriMayor = materiasPendientes[-1].cuatri
        cantidad = [0 for i in range (cuatriMayor)]

        for materia in materiasPendientes:
            cantidad[materia.cuatri-1]+=1

        cuatri = cantidad.index(max(cantidad))
        return cuatri+1

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
