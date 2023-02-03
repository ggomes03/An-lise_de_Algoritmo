def insertion_sort(lista):
    for i in range(1, len(lista)):
        inserido = lista[i]
        j = i-1
        while j >= 0 and inserido < lista[j]:
                lista[j + 1] = lista[j]         # move o cada elemento pra sua posição correta
                j -= 1
        lista[j + 1] = inserido                      # atribui o valor inserido na sua posição correta
    return lista

    