def cycle_sort(arr):
    n = len(arr)
    
    for cycle_start in range(n - 1):
        item = arr[cycle_start]
        pos = cycle_start
        
        # Buscar la posición correcta para el elemento actual
        for i in range(cycle_start + 1, n):
            if arr[i] < item:
                pos += 1
        
        # Si la posición es la misma, no hay ciclo
        if pos == cycle_start:
            continue
        
        # Colocar el elemento en su posición correcta
        while item == arr[pos]:
            pos += 1
        arr[pos], item = item, arr[pos]
        
        # Continuar hasta que se complete el ciclo
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if arr[i] < item:
                    pos += 1
            while item == arr[pos]:
                pos += 1
            arr[pos], item = item, arr[pos]

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    cycle_sort(arr)
    print("Arreglo ordenado:")
    for item in arr:
        print(item)
