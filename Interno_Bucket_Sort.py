def bucket_sort(arr):
    # Encontrar el valor máximo y mínimo en la lista
    max_val, min_val = max(arr), min(arr)
    
    # Crear los cubos (buckets)
    num_buckets = max_val - min_val + 1
    buckets = [[] for _ in range(num_buckets)]

    # Colocar elementos en los cubos
    for num in arr:
        index = num - min_val
        buckets[index].append(num)

    # Ordenar cada cubo utilizando un algoritmo de ordenamiento (puedes usar cualquier algoritmo)
    sorted_arr = []
    for bucket in buckets:
        if bucket:
            bucket.sort()
            sorted_arr.extend(bucket)

    return sorted_arr

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = bucket_sort(arr)
    print("Arreglo ordenado:")
    for item in sorted_arr:
        print(item)
