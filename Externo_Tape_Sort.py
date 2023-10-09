import heapq
import os
import tempfile

# Función para fusionar bloques ordenados en una cinta
def merge_blocks_to_tape(input_blocks, output_tape):
    heap = []  # Un heap mínimo para realizar la fusión

    # Abrir todos los bloques ordenados e inicializar el heap
    for block in input_blocks:
        file = open(block, 'rb')
        item = int.from_bytes(file.read(4), byteorder='big', signed=False)
        heap.append((item, file))

    # Fusionar los bloques ordenados en la cinta de salida
    with open(output_tape, 'wb') as outfile:
        while heap:
            min_item, file = heapq.heappop(heap)
            outfile.write(min_item.to_bytes(4, byteorder='big'))
            next_item = int.from_bytes(file.read(4), byteorder='big', signed=False)
            if next_item:
                heapq.heappush(heap, (next_item, file))
            else:
                file.close()
                os.remove(file.name)

# Función principal para Tape Sort
def tape_sort(input_tape, output_tape, block_size, num_tapes):
    # Dividir el archivo en bloques y ordenarlos en cintas temporales
    temp_tapes = []
    for i in range(num_tapes):
        block = []
        with open(input_tape, 'rb') as infile:
            while len(block) < block_size:
                item = infile.read(4)
                if not item:
                    break
                block.append(int.from_bytes(item, byteorder='big', signed=False))
        
        block.sort()
        with tempfile.NamedTemporaryFile(delete=False) as tmpfile:
            for item in block:
                tmpfile.write(item.to_bytes(4, byteorder='big'))
            temp_tapes.append(tmpfile.name)

    # Fusionar las cintas temporales en la cinta de salida
    merge_blocks_to_tape(temp_tapes, output_tape)

# Ejemplo de uso:
if __name__ == "__main__":
    input_tape = "input_tape.dat"  # Nombre de la cinta de entrada
    output_tape = "output_tape.dat"  # Nombre de la cinta de salida
    block_size = 1000  # Tamaño del bloque en elementos
    num_tapes = 4  # Número de cintas disponibles
    
    tape_sort(input_tape, output_tape, block_size, num_tapes)
    print("Cinta ordenada y guardada en", output_tape)
