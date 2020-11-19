from modules.lectorExcel import Lector
from modules.asignador import Asignador

l = Lector('../testData/datosPrincipales.xlsx', '../testData/datosAdicionales.xlsx', '../testData/mapasCurriculares.xlsx')
materias = l.extraerMaterias()
alumnos = l.extraerAlumnos(materias)
programas = l.extraerProgramas()

asignador = Asignador(alumnos, programas, materias)
asignador.crearGrupos()
