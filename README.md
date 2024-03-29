# pps_python_git_docker

Esta es una aplicación que proporciona mensajes al estilo de galleta de la fortuna

## Resolución de Dependencias

Para que no hayan errores y todo este correcto seguir estos pasos:

1. **Instalación de Python:**
   Con el comando apt install python

2. **Crear un Entorno Virtual:**
   Para crear el entorno aislado:
   
   python -m venv entorno_virtual_galleta_fortuna

   para activar el entorno:
   entorno_virtual_galleta_fortuna/bin/activate

3. **Dependencias**
    Para exportar las dependencias usamos este comando:
    pip freeze > requirements.txt
    
    Para importar las dependencias usamos este:
    pip install -r requirements.txt
4. **Ejecutar aplicacion**
    python app.py esto muestra "hola, mundo"

6. **Puesta en común**
   - 1. Clonar repositorio:
    git@github.com:dhcmurciaeduca/pps_python_git_docker.git

   - 2. Cambiar al repositorio:
    cd nombre_del_repositorio
   
   - 3. Configurar Entorno:
    Instala Python. Seguir pasos del P1**Instalación de Python:**

    Crea un entorno virtual. Seguir pasos del P2**Crear un Entorno Virtual:**
    
    Instala las dependencias del proyecto: Seguir pasos del P3**Dependencias**

   - 4. Desarrollo:
    Crear rama:
    git checkout -b nueva_rama...
    Cada colaborador trabaja en su rama correspondiente.

    Realizar cambios y asegurarse de que funcionan, una vez hecho subir cambios:
    git add .
    git commit -m "Mensaje commit"
    

   -Sube tus cambios a GitHub:
    git push origin rama_nueva...

8. **Despliegue seguro**
   - 1. Crea/Descarga fichero Dockerfile multifase(dockerfile).
   - 2. Crea/Descarga el fichero .dockerignore(.dockerignore)
   - 3. Construye la imagen, despliega un contenedor y prueba que funcione.
      - 1. docker build -t pps_contenedor .
      - 2. docker run -d --name pps_contenedor -p 5001:5000 pps_contenedor
9. **Despliegue correcto en contenedor docker**
   - 1. apt update
   - 2. apt install curl
   - 3. apt install nano

10. **Redes y MongoDB**
   - 1. Levanta un contenedor con la imagen de Mongo. Búscala en https://hub.docker.com:
   docker run --name mongoimg -d mongo

   - 2. Dentro de la carpeta del proyecto pps_python_git_docker/
   ejecutar el comando: docker build -t pps_contenedor . 
   y luego ejecutar: docker run -d --name pps_contenedor -p 5000:5000 pps_contenedor

   - 3. Conectamos ambos contenedores a la misma red con estos comandos:
   docker network create red
   docker network connect red mongoimg
   docker network connect red pps_contenedor


   
11. **DOCKER COMPOSE**
   1. Instalar Docker-compose. apt install docker-compose
   2. Descargar el "compose.yml" para desplegar ambos contenedores simultaneamente.
   3. Modificación en el .dockerignore para que no copie "compose.yml"
   4. Ejecutar docker-compose up

12. **12. Añadir frases auspiciosas**
   1. Ejecutar para añadir nuevas frases: curl -X POST -H "Content-Type: application/json" -d '{"frases": ["Nueva frase 1 añadida a la base de datos", "Nueva frase 2 añadida a la base de datos"]}' http://localhost:5000/frotar/add
   2. Se han modificado bayeta.py y app.py para crear un nuevo endppoint que llame a la funcion que inserta frases en la base de datos.
