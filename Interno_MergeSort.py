def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    # Dividir la lista en mitades
    middle = len(arr) // 2
    left_half = arr[:middle]
    right_half = arr[middle:]

    # Aplicar MergeSort de manera recursiva a ambas mitades
    left_half = merge_sort(left_half)
    right_half = merge_sort(right_half)

    # Combinar las dos mitades ordenadas
    sorted_arr = merge(left_half, right_half)
    return sorted_arr

def merge(left, right):
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = merge_sort(arr)
    print("Arreglo ordenado:")
    for item in sorted_arr:
        print(item)
