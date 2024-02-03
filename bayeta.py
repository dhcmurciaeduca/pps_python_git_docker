import random

def frotar(n_frases: int = 1) -> list:
    with open('pps_python_git_docker/frases.txt', 'r') as archivo:
        lista_de_frases = archivo.readlines()
    
    
    lista_de_frases = [frase.strip() for frase in lista_de_frases]
    
    
    frases_elegidas = random.sample(lista_de_frases, n_frases)
    
    return frases_elegidas

