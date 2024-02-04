import os
import random

def frotar(n_frases: int = 1) -> list:
    # Obtener el directorio del script actual
    script_dir = os.path.dirname(__file__)
    # Construir la ruta al archivo frases.txt
    frases_file = os.path.join(script_dir, 'frases.txt')
    
    with open(frases_file, 'r') as archivo:
        lista_de_frases = archivo.readlines()
    
    lista_de_frases = [frase.strip() for frase in lista_de_frases]
    
    frases_elegidas = random.sample(lista_de_frases, n_frases)
    
    return frases_elegidas
