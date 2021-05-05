
<h1 align="center">
  <br>
  Plano
  <br>
</h1>

<h4 align="center">Formación de grupos y creación de horarios para directores de carrera UAG.</h4>

<p align="center">
  <a href="#descripción">Descripción</a> •
  <a href="#tecnologías">Tecnologías</a> •
  <a href="#correr-localmente">Correr Localmente</a> •
  <a href="#licencia">Licencia</a>

</p>

<h3 align="center">
  <img src="images/demo-plano.gif" width: 200px;"/>
</h3>

## Descripción

Se buscaba una solución para automatizar el proceso de formación de grupos y la creación de horarios, brindando una ayuda a los directores de carrera de la UAG.

### ¿Cómo funciona?

Se ingresan 3 archivos con la información relevante
- **Datos Principales:** Esta es una lista de los alumnos con las materias de su carrera, y sus calificaciones de materias que ya ha cursado.
- **Datos Adicionales:** En una hoja se tiene la información referente a las materias que debe tomar un alumno dependiendo de su carrera y el cuatrimestre que está cursando. En la segunda hoja, se tiene información acerca de los prerequisitos de cada materia.
- **Mapas Curriculares:** Las materias que conforman una carrera separadas por cuatrimestre, especificando las horas por semana al igual que si dicha materia requiere laboratorio.


Una vez cargados estos archivos, el programa comienza el análisis y crea grupos para cada materia intentando dar prioridad a las materias de los primeros cuatrimestres, pero al mismo tiempo procurando que se cubran la mayór cantidad de materias y alumnos.j

#### Guardar

Una vez hecho el análisis, este se puede guardar en un archivo .horario (que es una archivo JSON) de manera que se pueda cargar después sin tener que realizar en análisis de nuevo.

También se puede exportar en un archivo de excel, en un formato que les es conveniente a los directores de carrera.

## Tecnologías

Este proyecto fue desarrollado enteramente en **Python**, utilizando [PyQt5](https://doc.qt.io/qtforpython/) para la interfaz gráfica y [openpyxl](https://openpyxl.readthedocs.io/en/stable/) para la lectura y escritura de archivos de excel.

## Correr Localmente

Para correr esta aplcación localmente, necesitarás [Git](https://git-scm.com) y [Python 3](https://www.python.org/).

```bash
# Clonar este repositorio
$ git clone https://github.com/064xp/plano
# Entrar en directorio
$ cd plano
# Instalar dependencias
$ pip install -r requirements.txt
# Correr la aplicaión
$ cd src
$ python3 main.py
```
## Licencia

GPL-3.0
