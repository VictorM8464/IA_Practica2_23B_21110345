import tempfile
import os

# Función para dividir el archivo en bloques y ordenarlos en memoria
def sort_and_write_block(block, block_size):
    block.sort()
    with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
        for item in block:
            tmpfile.write(item.to_bytes(4, byteorder='big'))  # Asumiendo enteros de 4 bytes

# Función para fusionar bloques ordenados
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

# Función principal para Distribution Sort
def distribution_sort(input_file, output_file, block_size):
    sorted_blocks = []

    with open(input_file, 'rb') as infile:
        block = []
        item = infile.read(4)
        while item:
            block.append(int.from_bytes(item, byteorder='big', signed=False))
            if len(block) == block_size:
                sort_and_write_block(block, block_size)
                sorted_blocks.append(block.name)
                block = []
            item = infile.read(4)

        if block:
            sort_and_write_block(block, len(block))
            sorted_blocks.append(block.name)

    merge_sorted_blocks(sorted_blocks, output_file)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "input.txt"  # Nombre del archivo de entrada
    output_file = "output.txt"  # Nombre del archivo de salida
    block_size = 1000  # Tamaño del bloque en elementos
    
    distribution_sort(input_file, output_file, block_size)
    print("Archivo ordenado y guardado en", output_file)
