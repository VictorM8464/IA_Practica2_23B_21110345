import os
import tempfile
import math

# Función para dividir el archivo en cubetas según el dígito en la posición especificada
def distribute_to_buckets(input_file, output_files, digit_position):
    with open(input_file, 'rb') as infile:
        for i in range(256):
            output_files[i] = tempfile.NamedTemporaryFile(delete=False)

        item = infile.read(4)
        while item:
            value = int.from_bytes(item, byteorder='big', signed=False)
            digit = (value >> (8 * digit_position)) & 0xFF
            output_files[digit].write(item)
            item = infile.read(4)

    for i in range(256):
        output_files[i].close()

# Función para fusionar los archivos temporales en el archivo de salida
def merge_temp_files(input_files, output_file):
    heap = []  # Un heap mínimo para realizar la fusión

    for i, file in enumerate(input_files):
        item = int.from_bytes(file.read(4), byteorder='big', signed=False)
        if item:
            heapq.heappush(heap, (item, i, file))
        else:
            file.close()
            os.remove(file.name)

    with open(output_file, 'wb') as outfile:
        while heap:
            min_item, file_idx, file = heapq.heappop(heap)
            outfile.write(min_item.to_bytes(4, byteorder='big'))
            next_item = int.from_bytes(file.read(4), byteorder='big', signed=False)
            if next_item:
                heapq.heappush(heap, (next_item, file_idx, file))
            else:
                file.close()
                os.remove(file.name)

# Función principal para Radix Sort Externo
def radix_sort_external(input_file, output_file):
    temp_files = [None] * 256  # Un archivo temporal para cada cubeta

    # Determinar el número de dígitos en los elementos del archivo
    num_digits = int(math.ceil(math.log(256, 2)))

    for digit_position in range(num_digits):
        distribute_to_buckets(input_file, temp_files, digit_position)
        merge_temp_files(temp_files, input_file)

    os.rename(input_file, output_file)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "input.txt"  # Nombre del archivo de entrada
    output_file = "output.txt"  # Nombre del archivo de salida
    
    radix_sort_external(input_file, output_file)
    print("Archivo ordenado y guardado en", output_file)
