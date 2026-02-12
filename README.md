Gestor de tareas / incidencias - Prácticas 1º DAM
Aplicación web desarrollada en Python usando Flask , SQLite , HTML y CSS como parte del período de prácticas en empresa.

El objetivo del proyecto es aprender los fundamentos de Python aplicado a una aplicación web real, así como el uso básico de control de versiones con Git.

Este proyecto tiene un enfoque formativo y práctico, no se busca complejidad extrema ni soluciones perfectas, sino:

Entender cómo funciona una aplicación web

Aprender Python desde cero

Aplicar buenas prácticas básicas de desarrollo.

Trabajar como en un entorno real de empresa

📌 Descripción del proyecto
La aplicación consiste en un gestor sencillo de taras o incidencias , que permite:

Crear nuevas tareas
Listar todas las tareas existentes
Consultar el detalle de una tarea
Cambiar el estado de una tarea
Los datos se almacenan de forma persistente en una base de datos SQLite .

🛠️ Tecnologías utilizadas
Python 3
Matraz
SQLite
HTML
CSS
Git
Código de Visual Studio
📂 Estructura del proyecto
- task-manager/
    - app.py
    - database.db
    - requirements.txt
    - templates/
        - base.html
        - list.html
        - create.html
        - detail.html
    - static/
        - style.css
⚙️ Requisitos previos
Tener instalado Python 3
Tener instalado Git
Usar Visual Studio Code como editor de desarrollo
🚀 Puesta en marcha del proyecto
1️⃣ Clonar proyecto desde GitHub a directorio local
El primer paso será acceder a la URL del repositorio ( https://github.com/sercha30/task_manager_1_dam.git ) y realizar un clon del repositorio de forma local, para poder trabajar con el.

2️⃣ Abrir el proyecto
Abrir la carpeta del proyecto en Visual Studio Code .

3️⃣ Cambiar a la rama "desarrollar" y crear rama personal
Usando el terminal de Windows o el control de versiones integradas en VSC, crea una nueva rama para el trabajo personal en el proyecto con el formato development/apellidos_nombre . Esta es la rama que deberéis usar en todo momento para subir vuestros cambios.

Nunca usar otras ramas, si no se indica lo contrario .

4️⃣ Crear entorno virtual
Para aislar las dependencias que vas a usar, cread un entorno virtual para el proyecto usando el comando en el terminal de Windows:

python -m venv .venv
Después de esto, deberéis de activar el entorno virtual con el comando:

.venv\Scripts\activate
5️⃣ Instalar dependencias
El siguiente paso es instalar las dependencias necesarias para poder trabajar con el proyecto, que en este caso, vienen listadas en el archivo requisitos.txt dentro de la carpeta del proyecto. Para ello, basta con ejecutar el siguiente comando:

pip install -r requirements.txt
IMPORTANTE: Debes ejecutar el comando desde la carpeta raíz del proyecto para que funcione.

6️⃣ Ejecutar la aplicación
Podéis hacer una prueba rápida de que todo está bien configurado. Para ello, primero debéis de ejecutar la aplicación con el comando:

python app.py
Una vez arrancada, debéis abrir el navegador y acceder a la URL http://127.0.0.1:5000 , donde veréis una página con un error 404 (esto es normal porque aún no habéis añadido los endpoints correspondientes).

7️⃣ Base de datos
La aplicación utiliza SQLite para guardar las tareas que se crean. El archivo que usa la base de datos para guardar los datos es Database.db . La base de datos será gestionada directamente desde Python.

La tabla principal, llamada task , deberá tener los siguientes campos:

identificación
título
descripción
estado
creado_en
8️⃣ Control de versiones
Este proyecto debe versionarse usando Git , que es una de las herramientas de control de versiones más usadas a nivel profesional en la actualidad.

Durante el desarrollo del proyecto deben de seguirse una serie de buenas prácticas a la hora de realizar el control de versiones:

Usar únicamente el repositorio facilitado.
Realizar commits frecuentes (por lo general, un commit por funcionalidad).
Realizar un push a la rama personal al final del día para no perder el trabajo del día.
Los mensajes de compromiso deben ser claros y descriptivos.
Ejemplos de commits:

Initial project structure
Add task creation form
Implement SQLite database
Add task status update
9️⃣ Entregables
Se considera el proyecto finalizado una vez que los siguientes entregables se encuentren en el repositorio, subidos a vuestra rama personal:

Código fuente del proyecto
Base de datos SQLite
Documento README (diferente a este) explicando:
Cómo ejecutar el proyecto
Qué funcionalidades incluye
Ideas sobre posibles nuevas funcionalidades o mejoras.
🆙 OPCIONAL: Funcionalidades adicionales
Si habéis terminado las funcionalidades principales y queréis ampliar conocimientos e ir un poco más allá, se proponen las siguientes mejoras:

Filtros por estado
Validaciones de formularios
Mejora visual con CSS
Mensajes de confirmación de error
Visualizar la base de datos en un cliente de base de datos
Podéis intentar realizar estas tareas por vuestra cuenta y ver hasta dónde sois capaces de llegar 😉
