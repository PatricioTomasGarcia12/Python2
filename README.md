Patricio Tomás García 23787/4

Para ejecutar el ejercio 10, se debe tener instaladas las dependencias especificadas en el requirements.txt.

Es recomendable utilizar un entorno virtual para evitar conflictos con diferentes versiones de las dependencias que puede necesitar para otros proyectos.

Para crear un entorno virtual demos ejecutar el comando “python –m venv” y el nombre de la carpeta donde queremos crear el entorno virtual por convención se usa .venv, es recordable usar este nombre para que los ides puedan reconocerla. Una vez creado el entorna debemos activarlo con el comando  “.\nombre_entorno\Scripts\activate” en Windows o con el comando “.venv/bin/activate” en Linux, una vez activado debemos ver el texto (.venv) en la consola

Una vez que este activado el entorno virtual con el comando “pip install –r requirements.txt” el comando puede dar error en Windows “pip install '–r requirements.txt” eso soluciona el error haciendo que PowerShell interprete el  –r como un comando instalamos todas las dependencias necesarias en la versión que se usaron para crear el ejerció 10 

Una vez instaladas las dependencias abrimos el archivo ejercicios.ipynb que está en la carpeta notebooks y ejecutamos los tres bloques de código en orden, en el primero importamos el módulo sys y lo usamos para añadir la ruta donde está el código del ejercicio para poder hacer el import, en el segundo hacemos el import y en el tercer ejecutamos la función main del ejercicio.

Una vez que terminemos de ejecutar el programa podemos usar el comando deactivate para desactivar el entorno virtual

