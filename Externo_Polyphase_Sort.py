import os
import heapq
import tempfile
import shutil

# Función para mezclar fases de secuencias en una nueva fase
def merge_phase(phase_files, output_file):
    heap = []

    # Abre los archivos de fase y agrega el primer elemento de cada archivo al montículo
    for i, file_name in enumerate(phase_files):
        with open(file_name, 'r') as f:
            first_element = int(f.readline().strip())
            heapq.heappush(heap, (first_element, i, f))

    # Crea el archivo de salida para la fase
    with open(output_file, 'w') as output:
        while heap:
            smallest, file_index, file_handle = heapq.heappop(heap)
            output.write(str(smallest) + '\n')

            next_element = file_handle.readline().strip()
            if next_element:
                next_element = int(next_element)
                heapq.heappush(heap, (next_element, file_index, file_handle))

# Función principal para ordenar externamente un archivo utilizando Polyphase Sort
def polyphase_sort(input_file, output_file, phase_size):
    # Divide y ordena las fases iniciales
    phase = 0
    chunk_files = [input_file]
    phase_files = []

    while chunk_files:
        phase += 1
        output_dir = tempfile.mkdtemp()
        phase_files = []

        for i in range(0, len(chunk_files), phase_size):
            chunk_group = chunk_files[i:i + phase_size]
            temp_output = os.path.join(output_dir, f'phase_{phase}_file_{i // phase_size}')
            merge_phase(chunk_group, temp_output)
            phase_files.append(temp_output)

        # Libera los archivos de la fase anterior
        for file in chunk_files:
            os.remove(file)

        chunk_files = phase_files

    # Renombra el archivo resultante al archivo de salida
    shutil.move(phase_files[0], output_file)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "large_input.txt"  # Cambia esto al nombre de tu archivo de entrada
    output_file = "sorted_output.txt"  # Cambia esto al nombre de tu archivo de salida
    phase_size = 10  # Tamaño de la fase, ajusta según sea necesario
    polyphase_sort(input_file, output_file, phase_size)
    print(f"Archivo '{input_file}' ordenado y guardado en '{output_file}'.")
