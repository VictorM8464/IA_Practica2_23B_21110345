import heapq
import tempfile
import shutil

# Función para fusionar dos secuencias ordenadas en una sola secuencia ordenada
def merge_sequences(seq1, seq2):
    merged_sequence = []
    while seq1 and seq2:
        if seq1[0] <= seq2[0]:
            merged_sequence.append(seq1.pop(0))
        else:
            merged_sequence.append(seq2.pop(0))
    return merged_sequence + seq1 + seq2

# Función para dividir una secuencia en secuencias ordenadas
def split_sequences(sequence):
    sequences = []
    current_sequence = [sequence[0]]

    for i in range(1, len(sequence)):
        if sequence[i] >= sequence[i - 1]:
            current_sequence.append(sequence[i])
        else:
            sequences.append(current_sequence)
            current_sequence = [sequence[i]]

    sequences.append(current_sequence)
    return sequences

# Función principal para ordenar externamente un archivo
def external_sort(input_file, output_file):
    # Leer el archivo de entrada y dividirlo en secuencias ordenadas
    with open(input_file, 'r') as f:
        sequence = [int(line.strip()) for line in f]
    sequences = split_sequences(sequence)

    # Fusionar secuencias ordenadas hasta que quede una sola secuencia
    while len(sequences) > 1:
        new_sequences = []
        i = 0
        while i < len(sequences):
            if i + 1 < len(sequences):
                merged_sequence = merge_sequences(sequences[i], sequences[i + 1])
                new_sequences.append(merged_sequence)
                i += 2
            else:
                new_sequences.append(sequences[i])
                i += 1
        sequences = new_sequences

    # Escribir la secuencia ordenada en el archivo de salida
    with open(output_file, 'w') as f:
        for item in sequences[0]:
            f.write(str(item) + '\n')

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "large_input.txt"  # Cambia esto al nombre de tu archivo de entrada
    output_file = "sorted_output.txt"  # Cambia esto al nombre de tu archivo de salida
    external_sort(input_file, output_file)
    print(f"Archivo '{input_file}' ordenado y guardado en '{output_file}'.")
