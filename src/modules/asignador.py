class Asignador:

    def asignarMaterias(self, materias, alumnos, programas):
        for alumno in alumnos:
            materias = alumno.materiasPendientes[0:10]
            cuatri = self.promediarCuatri(materias)
            materiasPorCuatri = programas[alumno.carrera][cuatri-1]
            materias = alumno.materiasPendientes[0:materiasPorCuatri]

            for materia in materias:
                materia.alumnos.append(alumno.registro)

    # def promediarCuatri(self, materiasPendientes):
    #     sumaCuatri = 0
    #     for materia in materiasPendientes:
    #         sumaCuatri+= materia.cuatri
    #     promedio = int(sumaCuatri/len(materiasPendientes))
    #
    #     return promedio

def calcularCuatri(self,materiasPendientes):
    cuatriMayor = 0
    cantidadMaterias = 0
    cuatri = 0
    cantidad = []
    for materia in materiasPendientes:
        if cuatriMayor < materia.cuatri:
            cuatriMayor = materia.cuatri
        else:
            continue

    for i in range(cuatriMayor):
        cantidad.append(0)

    for materia in materiasPendientes:
        if cantidad[materia.cuatri-1] >= 1:
            cantidad[materia.cuatri-1]+=1

        else:
            cantidad[materia.cuatri-1] = 1

    for i in range(len(cantidad)):
       if cantidadMaterias < cantidad[i]:
           cantidadMaterias = cantidad[i]
           cuatri = i

    return cuatri+1
