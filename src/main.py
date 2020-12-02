from modules.lectorExcel import Lector
from modules.asignadorGrupos import AsignadorGrupos

l = Lector('../testData/datosPrincipales.xlsx', '../testData/datosAdicionales.xlsx', '../testData/mapasCurriculares.xlsx')
materias = l.extraerMaterias()
alumnos = l.extraerAlumnos(materias)
programas = l.extraerProgramas()

asignador = AsignadorGrupos(alumnos, programas, materias)
asignador.crearGrupos()
