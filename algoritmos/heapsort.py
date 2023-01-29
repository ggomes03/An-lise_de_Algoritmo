def CorrigeHeapSort(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[i] < arr[left]:
        largest = left

    if right < n and arr[largest] < arr[right]:
        largest = right

    if largest != i:
        aux = arr[i]
        arr[i] = arr[largest]
        arr[largest] = aux
        CorrigeHeapSort(arr, n, largest)


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