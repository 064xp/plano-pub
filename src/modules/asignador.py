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
    cantidad = []
    cuatriMayor = materiasPendientes[-1].cuatri
    cantidad = [0 for i in range (cuatriMayor)]

    for materia in materiasPendientes:
        cantidad[materia.cuatri-1]+=1

    cuatri = cantidad.index(max(cantidad))

    return cuatri+1
