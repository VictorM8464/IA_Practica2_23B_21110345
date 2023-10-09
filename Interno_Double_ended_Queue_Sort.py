from collections import deque

def dequeue_sort(arr):
    # Crear una deque a partir de la lista desordenada
    deq = deque(arr)
    
    # Ordenar la deque (esto ordenará la lista original)
    deq = deque(sorted(deq))
    
    # Convertir la deque ordenada nuevamente en una lista
    sorted_arr = list(deq)
    
    return sorted_arr

# Ejemplo de uso:
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr = dequeue_sort(arr)
    print("Arreglo ordenado:")
    for item in sorted_arr:
        print(item)
