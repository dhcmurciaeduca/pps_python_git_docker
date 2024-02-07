import os
import random
from pymongo import MongoClient

def frotar(n_frases: int = 1) -> list:
    # Obtener el directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta al archivo frases.txt
    frases_file = os.path.join(script_dir, 'frases.txt')
    
    # Leer el contenido del archivo frases.txt
    with open(frases_file, 'r') as archivo:
        lista_de_frases = [frase.strip() for frase in archivo.readlines()]

    # Conexión con el motor de Mongo (nombre del contenedor de Mongo: "nombre_del_contenedor_mongo")
    cliente_mongo = MongoClient('mongodb://mongoimg:27017/')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la colección (en MongoDB se llama "colección" en lugar de "tabla")
    frases_auspiciosas = bd['frases_auspiciosas']
    
    # Comprobar si la colección está vacía antes de insertar los datos
    if frases_auspiciosas.count_documents({}) == 0:
        # Insertar el contenido del archivo frases.txt en la colección
        datos = [{"frase": frase} for frase in lista_de_frases]
        frases_auspiciosas.insert_many(datos)
        print("Datos insertados en la base de datos MongoDB.")
    else:
        print("La colección ya contiene datos. No se realizaron inserciones.")

    # Obtener frases aleatorias
    frases_aleatorias = obtener_frases_mongo(n_frases)
    
    # Cerrar cliente
    cliente_mongo.close()
    
    return frases_aleatorias

def obtener_frases_mongo(n_frases: int) -> list:
    # Conexión con el motor de Mongo (nombre del contenedor de Mongo: "nombre_del_contenedor_mongo")
    cliente_mongo = MongoClient('mongodb://mongoimg:27017/')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la colección (en MongoDB se llama "colección" en lugar de "tabla")
    frases_auspiciosas = bd['frases_auspiciosas']
    
    # Obtener frases aleatorias
    frases_aleatorias = list(frases_auspiciosas.aggregate([{'$sample': {'size': n_frases}}]))
    
    # Cerrar cliente
    cliente_mongo.close()
    
    # Extraer las frases de la lista de documentos obtenidos
    frases = [frase['frase'] for frase in frases_aleatorias]
    
    return frases

def insertar_frases(frases: list):
    # Conexión con el motor de Mongo (nombre del contenedor de Mongo: "nombre_del_contenedor_mongo")
    cliente_mongo = MongoClient('mongodb://mongoimg:27017/')
    
    # Conexión con la BD (la crea si no existe)
    bd = cliente_mongo['bayeta']
    
    # Conexión con la colección (en MongoDB se llama "colección" en lugar de "tabla")
    frases_auspiciosas = bd['frases_auspiciosas']
    
    # Insertar las frases proporcionadas en la lista
    datos = [{"frase": frase} for frase in frases]
    frases_auspiciosas.insert_many(datos)
    print("Frases insertadas en la base de datos MongoDB.")
    
    # Cerrar cliente
    cliente_mongo.close()

