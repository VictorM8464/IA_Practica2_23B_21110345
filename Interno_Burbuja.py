def bubble_sort(arr):
    n = len(arr)
    
    for i in range(n):
        # El último 'i' elementos ya están en su lugar
        for j in range(0, n-i-1):
            # Intercambiar si el elemento encontrado es mayor que el siguiente elemento
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    bubble_sort(arr)
    print("Arreglo ordenado:")
    for i in range(len(arr)):
        print(arr[i])
