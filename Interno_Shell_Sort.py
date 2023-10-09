def shell_sort(arr):
    n = len(arr)
    gap = n // 2  # Inicializar el espacio de brecha

    while gap > 0:
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2  # Reducir la brecha a la mitad en cada iteración

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    shell_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
