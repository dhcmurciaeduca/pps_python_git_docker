import os
import random
from pymongo import MongoClient

def frotar(n_frases: int = 1) -> list:
    # Obtener el directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta al archivo frases.txt
    frases_file = os.path.join(script_dir, 'frases.txt')
    
    with open(frases_file, 'r') as archivo:
        lista_de_frases = archivo.readlines()
    
    lista_de_frases = [frase.strip() for frase in lista_de_frases]
    
    # Llamar al método del fichero de Mongo
    frases_aleatorias = obtener_frases_mongo(n_frases)
    
    return frases_aleatorias

def obtener_frases_mongo(n_frases: int) -> list:
    # Conexión con el motor de Mongo (nombre del contenedor de Mongo: "nombre_del_contenedor_mongo")
    cliente_mongo = MongoClient('mongodb://mi_mongo:27017/')
    
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
