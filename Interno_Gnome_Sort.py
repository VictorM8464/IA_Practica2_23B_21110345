def gnome_sort(arr):
    index = 0
    n = len(arr)
    
    while index < n:
        if index == 0:
            index += 1
        if arr[index] >= arr[index - 1]:
            index += 1
        else:
            arr[index], arr[index - 1] = arr[index - 1], arr[index]
            index -= 1

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    gnome_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
