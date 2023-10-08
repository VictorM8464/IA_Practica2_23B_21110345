import heapq
import tempfile
import shutil

# Función para fusionar múltiples secuencias ordenadas en una sola secuencia ordenada
def multiway_merge(sorted_files, output_file):
    heap = []

    # Abre los archivos de entrada y agrega el primer elemento de cada archivo al montículo
    for i, file_name in enumerate(sorted_files):
        with open(file_name, 'r') as f:
            first_element = int(f.readline().strip())
            heapq.heappush(heap, (first_element, i, f))

    # Crea el archivo de salida
    with open(output_file, 'w') as output:
        while heap:
            smallest, file_index, file_handle = heapq.heappop(heap)
            output.write(str(smallest) + '\n')

            next_element = file_handle.readline().strip()
            if next_element:
                next_element = int(next_element)
                heapq.heappush(heap, (next_element, file_index, file_handle))

# Función para dividir y ordenar un archivo grande en múltiples archivos más pequeños
def split_and_sort(input_file, chunk_size):
    chunk_files = []

    with open(input_file, 'r') as f:
        chunk = []
        for line in f:
            chunk.append(int(line.strip()))
            if len(chunk) == chunk_size:
                chunk.sort()
                temp_file = tempfile.NamedTemporaryFile(delete=False)
                temp_file.writelines([str(item) + '\n' for item in chunk])
                temp_file.close()
                chunk_files.append(temp_file.name)
                chunk = []

        if chunk:
            chunk.sort()
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.writelines([str(item) + '\n' for item in chunk])
            temp_file.close()
            chunk_files.append(temp_file.name)

    return chunk_files

# Función principal para ordenar externamente un archivo
def external_sort(input_file, output_file, chunk_size, fanout):
    # Divide y ordena los chunks
    chunk_files = split_and_sort(input_file, chunk_size)

    # Realiza el ordenamiento balanceado multiway merging
    while len(chunk_files) > 1:
        new_chunk_files = []

        for i in range(0, len(chunk_files), fanout):
            chunk_group = chunk_files[i:i + fanout]
            temp_output = tempfile.NamedTemporaryFile(delete=False)
            multiway_merge(chunk_group, temp_output.name)
            new_chunk_files.append(temp_output.name)

        chunk_files = new_chunk_files

    # Renombra el archivo resultante al archivo de salida
    shutil.move(chunk_files[0], output_file)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "large_input.txt"  # Cambia esto al nombre de tu archivo de entrada
    output_file = "sorted_output.txt"  # Cambia esto al nombre de tu archivo de salida
    chunk_size = 1000  # Tamaño del chunk, ajusta según sea necesario
    fanout = 10  # Factor de ventilador, ajusta según sea necesario
    external_sort(input_file, output_file, chunk_size, fanout)
    print(f"Archivo '{input_file}' ordenado y guardado en '{output_file}'.")
