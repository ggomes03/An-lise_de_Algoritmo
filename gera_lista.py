import random

def gera_lista_sem_rep(n): #muito lento
    unique_list = []
    for i in range(n):
        new_number = random.randint(0, n*4)
        while new_number in unique_list:
            new_number = random.randint(0, n*4)
        unique_list.append(new_number)
    return unique_list

def random_unique_int_list(quantidade): # muito lento
    int_list = []
    while len(int_list) < quantidade:
        new_int = random.randint(0, quantidade * 2)
        if new_int not in int_list:
            int_list.append(new_int)
    return int_list


def cria_lista_aleatoria(quantidade): # bom 
    return random.sample(range(quantidade * 3), quantidade)

def cria_lista_quase_ordenada(tamanho):
    lista = [i for i in range(tamanho)]
    for i in range(tamanho//10):
        a = random.randint(0, tamanho-1)
        b = random.randint(0, tamanho-1)
        lista[a], lista[b] = lista[b], lista[a]
    return lista

def cria_lista_inversamente_ordenada(tamanho):
    return list(range(tamanho-1, -1, -1))

def cria_lista_ordenada(tamanho):
    return list(range(tamanho))

