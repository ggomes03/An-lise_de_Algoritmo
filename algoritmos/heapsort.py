def CorrigeHeapSort(arr, n, i):
    maior = i
    esq = 2 * i + 1
    dir = 2 * i + 2

    if esq < n and arr[i] < arr[esq]:
        maior = esq

    if dir < n and arr[maior] < arr[dir]:
        maior = dir

    if maior != i:
        aux = arr[i]
        arr[i] = arr[maior]
        arr[maior] = aux
        CorrigeHeapSort(arr, n, maior)


def heap_sort(arr):
    n = len(arr)

    for i in range(n, -1, -1):
        CorrigeHeapSort(arr, n, i)

    for i in range(n-1, 0, -1):
        aux = arr[i]
        arr[i] = arr[0]
        arr[0] = aux
        CorrigeHeapSort(arr, i, 0)

    return arr