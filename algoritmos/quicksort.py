def quicksort(lista):
    if len(lista) <= 1:
        return lista
    pivot = lista[len(lista) // 2]
    esquerda = [x for x in lista if x < pivot]
    meio = [x for x in lista if x == pivot]
    direita = [x for x in lista if x > pivot]
    return quicksort(esquerda) + meio + quicksort(direita)