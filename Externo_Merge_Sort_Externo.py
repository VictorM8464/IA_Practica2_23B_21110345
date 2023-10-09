import tempfile
import heapq
import os

# Función para dividir el archivo en runs (secuencias ordenadas)
def create_runs(input_file, run_size, buffer_size):
    runs = []
    with open(input_file, 'rb') as infile:
        while True:
            data = infile.read(run_size * buffer_size)
            if not data:
                break
            run = list(data)
            run.sort()
            runs.append(run)
    return runs

# Función para fusionar dos runs
def merge_runs(run1, run2):
    merged_run = []
    while run1 and run2:
        if run1[0] <= run2[0]:
            merged_run.append(run1.pop(0))
        else:
            merged_run.append(run2.pop(0))
    merged_run.extend(run1)
    merged_run.extend(run2)
    return merged_run

# Función principal para Merge Sort Externo
def merge_sort_external(input_file, output_file, buffer_size):
    run_size = buffer_size  # Tamaño inicial de los runs
    runs = create_runs(input_file, run_size, buffer_size)
    
    while len(runs) > 1:
        next_runs = []
        for i in range(0, len(runs), 2):
            if i + 1 < len(runs):
                merged_run = merge_runs(runs[i], runs[i + 1])
                next_runs.append(merged_run)
            else:
                next_runs.append(runs[i])
        runs = next_runs
        run_size *= 2
    
    with open(output_file, 'wb') as outfile:
        outfile.write(bytes(runs[0]))

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "input.txt"  # Nombre del archivo de entrada
    output_file = "output.txt"  # Nombre del archivo de salida
    buffer_size = 1000  # Tamaño del buffer en bytes
    
    merge_sort_external(input_file, output_file, buffer_size)
    print("Archivo ordenado y guardado en", output_file)
