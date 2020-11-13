class Asignador:

    def asignarMaterias(self, materias, alumnos, programas):
        for alumno in alumnos:
            materias = alumno.materiasPendientes[0:10]
            cuatri = self.promediarCuatri(materias)
            materiasPorCuatri = programas[alumno.carrera][cuatri-1]
            materias = alumno.materiasPendientes[0:materiasPorCuatri]

            for materia in materias:
                materia.alumnos.append(alumno.registro)

    def promediarCuatri(self, materiasPendientes):
        sumaCuatri = 0
        for materia in materiasPendientes:
            sumaCuatri+= materia.cuatri
        promedio = int(sumaCuatri/len(materiasPendientes))

        return promedio
