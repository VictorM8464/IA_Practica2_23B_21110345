def heapify(arr, n, i):
    largest = i  # Inicializar el nodo ra�z como el nodo m�s grande
    left = 2 * i + 1
    right = 2 * i + 2

    # Comprobar si el hijo izquierdo existe y es mayor que el nodo ra�z
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Comprobar si el hijo derecho existe y es mayor que el nodo ra�z o el hijo izquierdo
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Si el nodo m�s grande no es la ra�z, intercambiarlos
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Llamar recursivamente a heapify en el sub�rbol afectado
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)

    # Construir un heap m�ximo (reorganizar la lista)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Extraer elementos uno por uno desde el heap
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Intercambiar el elemento m�ximo con el �ltimo elemento
        heapify(arr, i, 0)  # Llamar a heapify en el mont�culo reducido

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    heap_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
