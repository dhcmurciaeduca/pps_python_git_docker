# Fase de resolución de dependencias
FROM python:3.9-slim AS builder

# Establecer directorio de trabajo
WORKDIR /app

# Copiar el archivo de requerimientos
COPY requirements.txt .

# Instalar dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Fase de ejecución
FROM python:3.9-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar solo los archivos necesarios de la fase de resolución de dependencias
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages

# Copiar tu aplicación
COPY . .

# Comando de inicio de la aplicación
CMD ["python", "app.py"]
