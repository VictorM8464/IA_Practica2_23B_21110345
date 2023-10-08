def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 25, 12, 22, 11]
    selection_sort(arr)
    print("Arreglo ordenado:")
    for i in range(len(arr)):
        print(arr[i])