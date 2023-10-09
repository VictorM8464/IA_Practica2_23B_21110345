import heapq
import os
import tempfile

# Función para fusionar bloques ordenados en el archivo de salida
def merge_sorted_blocks(sorted_blocks, output_file):
    heap = []  # Un heap mínimo para realizar la fusión

    # Abrir todos los bloques ordenados e inicializar el heap
    for block in sorted_blocks:
        file = open(block, 'rb')
        item = int.from_bytes(file.read(4), byteorder='big', signed=False)
        heap.append((item, file))

    # Fusionar los bloques ordenados en el archivo de salida
    with open(output_file, 'wb') as outfile:
        while heap:
            min_item, file = heapq.heappop(heap)
            outfile.write(min_item.to_bytes(4, byteorder='big'))
            next_item = int.from_bytes(file.read(4), byteorder='big', signed=False)
            if next_item:
                heapq.heappush(heap, (next_item, file))
            else:
                file.close()
                os.remove(file.name)

# Función principal para Replacement Selection
def replacement_selection(input_file, output_file, memory_size):
    sorted_blocks = []
    unsorted_blocks = []

    with open(input_file, 'rb') as infile:
        while True:
            block = []
            item = infile.read(4)
            while item and len(block) < memory_size:
                block.append(int.from_bytes(item, byteorder='big', signed=False))
                item = infile.read(4)
            
            block.sort()  # Ordenar el bloque en memoria
            if len(block) < memory_size:
                sorted_blocks.append(block)
                break
            else:
                sort_and_write_block(block, unsorted_blocks)
                sorted_blocks.append(block)

    while unsorted_blocks:
        block = unsorted_blocks.pop(0)
        item = infile.read(4)
        if item:
            item = int.from_bytes(item, byteorder='big', signed=False)
            if item < block[-1]:
                heapq.heappush(block, item)
                unsorted_blocks.append(block)
                block = heapq.heappop(block)
            else:
                sort_and_write_block(block, unsorted_blocks)
                sorted_blocks.append(block)

    merge_sorted_blocks(sorted_blocks, output_file)

# Función para ordenar un bloque y escribirlo en un archivo temporal
def sort_and_write_block(block, block_list):
    block.sort()
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        for item in block:
            tmpfile.write(item.to_bytes(4, byteorder='big'))
        block_list.append(tmpfile.name)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "input.txt"  # Nombre del archivo de entrada
    output_file = "output.txt"  # Nombre del archivo de salida
    memory_size = 1000  # Tamaño de la memoria disponible
    
    replacement_selection(input_file, output_file, memory_size)
    print("Archivo ordenado y guardado en", output_file)
