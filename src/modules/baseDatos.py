import sqlite3
from modules.funcionesAyuda import FuncionesAyuda as ayuda

class BaseDatos:
    def __init__(self, archivoDB):
        self.conn = sqlite3.connect(archivoDB)
        self.cursor = self.conn.cursor()
        self.crearTablas()

    def insertarAlumno(self, alumno):
        comando = '''
            INSERT INTO Alumnos (registro, carrera, cuatri)
                VALUES (?, ?, ?)
        '''
        self.cursor.execute(comando, (alumno.registro, alumno.carrera, alumno.cuatri))

    def insertarMateria(self, materia, materias):
        comandoMaterias = '''
            INSERT INTO Materias (nombre, idMateria, prerequisito, horasPorSemana, tieneLab)
                VALUES (?, ?, ?, ?, ?)
        '''
        if materia.prerequisito:
            prerequisito = materias[ayuda.normalizar(materia.prerequisito)].id
        else:
            prerequisito = None

        self.cursor.execute(comandoMaterias,
            (materia.nombre, materia.id, prerequisito, materia.horasPorSemana, materia.tieneLab))
        self.conn.commit()

        comandoMateriaCarrera = '''
            INSERT INTO MateriaCarrera (idMateria, carrera, cuatri)
                VALUES (?, ?, ?)
        '''
        carreras = []
        for carrera in materia.cuatri:
            carreras.append((materia.id, carrera, materia.cuatri[carrera]))

        self.cursor.executemany(comandoMateriaCarrera, carreras)
        self.conn.commit()

    def insertarGrupo(self, grupo):
        comando = '''
            INSERT INTO Grupos (idGrupo, registro, idMateria)
                VALUES (?, ?, ?)
        '''
        for alumno in grupo.alumnos:
            self.cursor.execute(comando, (grupo.id, alumno.registro, grupo.materia.id))
        self.conn.commit()
        self.insertarHorario(grupo)

    def insertarHorario(self, grupo):
        comando = '''
        INSERT INTO Horario (idGrupo, dia, hora)
            VALUES (?, ?, ?)
        '''

        horas = []
        for dia in grupo.horario:
            for hora in grupo.horario[dia]:
                horas.append((grupo.id, dia, hora))
        self.cursor.executemany(comando, horas)
        self.conn.commit()

    def crearTablas(self):
        script = '''
            CREATE TABLE IF NOT EXISTS Alumnos(
                registro int,
                carrera text,
                cuatri int
            );

            CREATE TABLE IF NOT EXISTS Materias(
                nombre text,
                idMateria int,
                prerequisito int,
                horasPorSemana int,
                tieneLab boolean
            );

            CREATE TABLE IF NOT EXISTS MateriaCarrera(
                idMateria int,
                carrera text,
                cuatri int
            );

            CREATE TABLE IF NOT EXISTS Grupos(
                idGrupo int,
                idMateria int
            );

            CREATE TABLE IF NOT EXISTS AlumnoGrupo(
                idGrupo int,
                registro int,
            );

            CREATE TABLE IF NOT EXISTS Horario(
                idGrupo int,
                dia int,
                hora int
            );
        '''

        self.cursor.executescript(script)
        self.conn.commit()
