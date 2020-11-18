class Asignador:
    def __init__(self, alumnos, programas):
        self.alumnos = alumnos
        self.programas = programas

    def asignarMaterias(self):
        for alumno in self.alumnos:
            materias = alumno.materiasPendientes[0:10]
            cuatri = self.calcularCuatri(materias)
            materiasPorCuatri = self.programas[alumno.carrera].materiasPorCuatri[cuatri-1]
            materias = alumno.materiasPendientes[0:materiasPorCuatri]

            for materia in materias:
                materia.alumnos.append(alumno.registro)

    def calcularCuatri(self, materiasPendientes):
        cantidad = []
        cuatriMayor = materiasPendientes[-1].cuatri
        cantidad = [0 for i in range (cuatriMayor)]

        for materia in materiasPendientes:
            cantidad[materia.cuatri-1]+=1

        cuatri = cantidad.index(max(cantidad))

        return cuatri+1
