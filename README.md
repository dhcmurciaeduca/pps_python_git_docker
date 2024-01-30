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

