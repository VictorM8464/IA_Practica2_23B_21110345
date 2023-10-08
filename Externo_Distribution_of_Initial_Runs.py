import heapq
import tempfile
import shutil

# Función para mezclar las ejecuciones iniciales en una sola ejecución
def merge_runs(run_files, output_file):
    heap = []

    # Abre los archivos de ejecución inicial y agrega el primer elemento de cada archivo al montículo
    for i, file_name in enumerate(run_files):
        with open(file_name, 'r') as f:
            first_element = int(f.readline().strip())
            heapq.heappush(heap, (first_element, i, f))

    # Crea el archivo de salida para la ejecución final
    with open(output_file, 'w') as output:
        while heap:
            smallest, file_index, file_handle = heapq.heappop(heap)
            output.write(str(smallest) + '\n')

            next_element = file_handle.readline().strip()
            if next_element:
                next_element = int(next_element)
                heapq.heappush(heap, (next_element, file_index, file_handle))

# Función principal para ordenar externamente un archivo utilizando Distribution of Initial Runs
def distribution_of_initial_runs_sort(input_file, output_file, run_size):
    # Divide el archivo en ejecuciones iniciales y las ordena por separado
    run = 1
    run_files = []
    output_dir = tempfile.mkdtemp()

    with open(input_file, 'r') as f:
        run_buffer = []

        for line in f:
            run_buffer.append(int(line.strip()))

            if len(run_buffer) == run_size:
                run_buffer.sort()
                temp_output = os.path.join(output_dir, f'run_{run}.txt')
                with open(temp_output, 'w') as run_output:
                    for item in run_buffer:
                        run_output.write(str(item) + '\n')
                run_files.append(temp_output)
                run_buffer = []
                run += 1

        # Manejar la última ejecución
        if run_buffer:
            run_buffer.sort()
            temp_output = os.path.join(output_dir, f'run_{run}.txt')
            with open(temp_output, 'w') as run_output:
                for item in run_buffer:
                    run_output.write(str(item) + '\n')
            run_files.append(temp_output)

    # Mezcla las ejecuciones iniciales para obtener la ejecución final
    merge_runs(run_files, output_file)

    # Limpia los archivos temporales
    shutil.rmtree(output_dir)

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "large_input.txt"  # Cambia esto al nombre de tu archivo de entrada
    output_file = "sorted_output.txt"  # Cambia esto al nombre de tu archivo de salida
    run_size = 1000  # Tamaño de la ejecución inicial, ajusta según sea necesario
    distribution_of_initial_runs_sort(input_file, output_file, run_size)
    print(f"Archivo '{input_file}' ordenado y guardado en '{output_file}'.")
