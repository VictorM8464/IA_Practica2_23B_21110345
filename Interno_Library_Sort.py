def library_sort(arr):
    n = len(arr)
    
    for i in range(1, n):
        key = arr[i]
        left, right = 0, i - 1

        # Realizar una búsqueda binaria para encontrar la posición de inserción
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] <= key:
                left = mid + 1
            else:
                right = mid - 1

        # Insertar el elemento en la posición correcta
        for j in range(i, left, -1):
            arr[j] = arr[j - 1]
        arr[left] = key

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    library_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
