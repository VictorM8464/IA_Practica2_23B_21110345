def odd_even_sort(arr):
    n = len(arr)
    sorted = False
    
    while not sorted:
        sorted = True
        for i in range(1, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False
        for i in range(0, n-1, 2):
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                sorted = False

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    odd_even_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
