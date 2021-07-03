from modules.definiciones.Grupo import Grupo
from modules.funcionesAyuda import FuncionesAyuda as ayuda

class AsignadorGrupos:
    def __init__(self, alumnos, programas, materias, minAlumnos = 10, maxAlumnos=26):
        self.alumnos = alumnos
        self.programas = programas
        self.materias = materias
        self.minAlumnos = minAlumnos
        self.maxAlumnos = maxAlumnos
        self.grupoActual = 1

    def crearGrupos(self):
        self.asignarMaterias()
        self.crearGruposEnOrden()
        self.crearGruposFueraOrden()

    def asignarMaterias(self):
        for alumno in self.alumnos:
            # Calcular cuatri en base a las primeras 10 materias
            materias = alumno.materiasPendientes[0:9]
            cuatri = self.calcularCuatri(materias, alumno.carrera, alumno.registro)
            alumno.cuatri = cuatri

            materiasPorCuatri = self.programas[alumno.carrera].materiasPorCuatri[cuatri-1]
            alumno.materiasPorCuatri = materiasPorCuatri
            # materias = alumno.materiasPendientes[0:materiasPorCuatri]
            materiasAsignadas = 0
            for materia in alumno.materiasPendientes:
                if materiasAsignadas == materiasPorCuatri:
                    break
                if self.cumpleConPrerequisitos(alumno, materia):
                    materia.alumnos.append(alumno)
                    materiasAsignadas += 1

            # for materia in materias:
            #     materia.alumnos.append(alumno)
    def calcularCuatri(self, materiasPendientes, programa, alumno):
        cantidad = []
        cuatriMayor = max(materiasPendientes, key = lambda materia : materia.cuatri[programa]).cuatri[programa]
        cantidad = [0 for i in range (cuatriMayor)]

        for materia in materiasPendientes:
                cantidad[materia.cuatri[programa]-1]+=1

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
                    and self.cumpleConPrerequisitos(alumno, materia)
                    and alumno.materiasPorCuatri > 0):
                    materia.alumnos.append(alumno)
            self.crearGruposDeMateria(materia)

    def crearGruposDeMateria(self, materia):
        grupos = []
        while len(materia.alumnos) >= self.minAlumnos:
            alumnosGrupo = materia.alumnos[:self.maxAlumnos]
            materia.alumnos = materia.alumnos[self.maxAlumnos:]
            grupos.append(Grupo(alumnosGrupo, materia, self.grupoActual))
            self.grupoActual += 1
        materia.grupos.extend(grupos)
        self.quitarAlumnosAsignados(grupos, materia)

    def quitarAlumnosAsignados(self, grupos, materia):
        for grupo in grupos:
            for alumno in grupo.alumnos:
                alumno.materiasPendientes.remove(materia)
                alumno.materiasAsignadas.append(ayuda.normalizar(materia.nombre))
                alumno.materiasPorCuatri -= 1

    def cumpleConPrerequisitos(self, alumno, materia):
        if materia.prerequisito is None:
            return True

        if(materia.prerequisito in alumno.materiasAsignadas):
            return False

        for materiaPendiente in alumno.materiasPendientes:
            if materia.prerequisito == ayuda.normalizar(materiaPendiente.nombre):
                return False
        return True
