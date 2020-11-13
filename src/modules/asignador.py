class Asignador:
    '''
    materias = {
        'IIS 2006':{
            'logica': Materia(),
            'algebra y geometria': Materia()
        },
        'IIS 2016':{
            'logica y filosofia': Materia(),
            'algebra y geometria': Materia()
        }
    }

    programas = {
    'IIS 2006': [4,2,3,5],
    'IIS 2016': [5, 6, 4, 3]
    }
    '''

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

'''
for alumno in alumnos:
  materiasPorCuatri = 3
  materiasPropuestas = alumno.materiasPendientes[:materiasPorCuatri]

  for mp in materiasPropuestas:
      materias[mp].alumnos.append(alumno.registro)
'''
