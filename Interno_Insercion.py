def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    insertion_sort(arr)
    print("Arreglo ordenado:")
    for i in range(len(arr)):
        print(arr[i])
