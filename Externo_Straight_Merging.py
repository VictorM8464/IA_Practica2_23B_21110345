import heapq
import tempfile
import shutil

# Función para fusionar dos archivos ordenados en uno solo
def merge_files(file1, file2, output_file):
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(output_file, 'w') as output:
        merge_heap = []

        # Leer el primer elemento de cada archivo y ponerlos en el montículo
        line1 = f1.readline().strip()
        line2 = f2.readline().strip()
        while line1 or line2:
            if line1:
                heapq.heappush(merge_heap, (line1, 1))
                line1 = f1.readline().strip()
            if line2:
                heapq.heappush(merge_heap, (line2, 2))
                line2 = f2.readline().strip()

            # Fusionar los elementos en orden en el archivo de salida
            while merge_heap:
                item, file_number = heapq.heappop(merge_heap)
                output.write(item + '\n')

# Función para dividir un archivo grande en múltiples archivos más pequeños y ordenarlos
def split_and_sort(input_file, chunk_size):
    chunk_files = []

    with open(input_file, 'r') as f:
        while True:
            chunk = []
            for _ in range(chunk_size):
                line = f.readline().strip()
                if not line:
                    break
                chunk.append(line)
            if not chunk:
                break

            # Ordenar y guardar el chunk en un archivo temporal
            chunk.sort()
            temp_file = tempfile.NamedTemporaryFile(delete=False)
            temp_file.writelines('\n'.join(chunk))
            temp_file.close()
            chunk_files.append(temp_file.name)

    return chunk_files

# Función principal para ordenar externamente un archivo
def external_sort(input_file, output_file, chunk_size):
    # Dividir y ordenar los chunks
    chunk_files = split_and_sort(input_file, chunk_size)

    # Fusionar los archivos ordenados en uno solo
    while len(chunk_files) > 1:
        merge_files(chunk_files.pop(0), chunk_files.pop(0), chunk_files.append(tempfile.NamedTemporaryFile(delete=False).name))

    # Renombrar el archivo resultante al archivo de salida
    shutil.move(chunk_files[0], output_file)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "large_input.txt"  # Cambia esto al nombre de tu archivo de entrada
    output_file = "sorted_output.txt"  # Cambia esto al nombre de tu archivo de salida
    chunk_size = 1000  # Tamaño del chunk, ajusta según sea necesario
    external_sort(input_file, output_file, chunk_size)
    print(f"Archivo '{input_file}' ordenado y guardado en '{output_file}'.")
