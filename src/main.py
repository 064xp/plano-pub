from modules.lectorExcel import Lector
from modules.asignadorGrupos import AsignadorGrupos
from modules.asignadorHorarios import AsignadorHorarios

l = Lector('../testData/datosPrincipales.xlsx', '../testData/datosAdicionales.xlsx', '../testData/mapasCurriculares.xlsx')
materias = l.extraerMaterias()
alumnos = l.extraerAlumnos(materias)
programas = l.extraerProgramas()

asignador = AsignadorGrupos(alumnos, programas, materias)
asignador.crearGrupos()
asignadorH = AsignadorHorarios(materias,7,10)
asignadorH.asignar()
#print(asignadorH.tblHorarios)

for materia in materias.values():
    for i,grupo in enumerate(materia.grupos):
        print(f'grupo: {i} de materia: {materia.nombre}')
        print('Horario:')
        for dia in grupo.horario:
            print('Dia', dia)
            print(grupo.horario[dia])
        for alumno in grupo.alumnos:
            print(f'Alumno:{alumno.registro}')
