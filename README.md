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
