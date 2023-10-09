def counting_sort(arr):
    # Encontrar el valor máximo en la lista
    max_value = max(arr)
    
    # Crear una lista auxiliar de conteo (inicializada con ceros)
    count = [0] * (max_value + 1)

    # Contar la frecuencia de cada elemento en la lista original
    for num in arr:
        count[num] += 1

    # Reconstruir la lista ordenada a partir de la lista de conteo
    sorted_arr = []
    for i in range(max_value + 1):
        if count[i] > 0:
            sorted_arr.extend([i] * count[i])

    return sorted_arr

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [4, 2, 2, 8, 3, 3, 1]
    sorted_arr = counting_sort(arr)
    print("Arreglo ordenado:")
    for item in sorted_arr:
        print(item)
