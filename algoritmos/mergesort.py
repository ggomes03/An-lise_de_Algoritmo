def merge_sort(arr):
    if len(arr) > 1:
        meio = len(arr) // 2
        esq = arr[:meio]    #cria um array pegando os dados do arr da posição 0 até o meio(incluso o meio).
        dir = arr[meio:]    #cria um array pegando os dados do arr da posição meio + 1(meio não incluso) até o fim.

        merge_sort(esq)
        merge_sort(dir)

        i = j = k = 0

        while i < len(esq) and j < len(dir):
            if esq[i] < dir[j]:
                arr[k] = esq[i]
                i += 1
            else:
                arr[k] = dir[j]
                j += 1
            k += 1

        while i < len(esq):
            arr[k] = esq[i]
            i += 1
            k += 1

        while j < len(dir):
            arr[k] = dir[j]
            j += 1
            k += 1
    return arr