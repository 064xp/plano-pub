from modules.definiciones.Grupo import Grupo

class Asignador:
    def __init__(self, alumnos, programas, materias, minAlumnos = 10, maxAlumnos=26):
        self.alumnos = alumnos
        self.programas = programas
        self.materias = materias
        self.minAlumnos = minAlumnos
        self.maxAlumnos = maxAlumnos

    def asignarMaterias(self):
        for alumno in self.alumnos:
            materias = alumno.materiasPendientes[0:10]
            cuatri = self.promediarCuatri(materias)
            materiasPorCuatri = self.programas[alumno.carrera].materiasPorCuatri[cuatri-1]
            materias = alumno.materiasPendientes[0:materiasPorCuatri]

            for materia in materias:
                materia.alumnos.append(alumno)

    def promediarCuatri(self, materiasPendientes):
        sumaCuatri = 0
        for materia in materiasPendientes:
            sumaCuatri+= materia.cuatri
        promedio = int(sumaCuatri/len(materiasPendientes))
        return promedio

    def crearGrupos(self):
        for llaveMateria in self.materias.keys():
            grupos = []
            materia = self.materias[llaveMateria]
            for alumno in materia.alumnos:
                alumno.materiasPendientes.remove(materia)
            while len(materia.alumnos) >= self.minAlumnos:
                alumnosGrupo = materia.alumnos[:self.maxAlumnos]
                materia.alumnos = materia.alumnos[self.maxAlumnos:]
                grupos.append(Grupo(alumnosGrupo, materia.nombre))

            materia.grupos = grupos
