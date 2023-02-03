def selection_sort(lista):
    for i in range(len(lista)):
        min_index = i
        for j in range(i+1, len(lista)):
            if lista[j] < lista[min_index]:
                min_index = j
        aux = lista[min_index]
        lista[min_index] = lista[i]
        lista[i] = aux
    return lista

    