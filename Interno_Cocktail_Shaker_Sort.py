def cocktail_shaker_sort(arr):
    n = len(arr)
    swapped = True
    
    while swapped:
        swapped = False
        
        # Realizar un recorrido hacia adelante (izquierda a derecha)
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                arr[i], arr[i + 1] = arr[i + 1], arr[i]
                swapped = True
        
        # Si no hubo intercambios en el primer recorrido, la lista está ordenada
        if not swapped:
            break
        
        # Realizar un recorrido hacia atrás (derecha a izquierda)
        swapped = False
        for i in range(n - 1, 0, -1):
            if arr[i] < arr[i - 1]:
                arr[i], arr[i - 1] = arr[i - 1], arr[i]
                swapped = True

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    cocktail_shaker_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
