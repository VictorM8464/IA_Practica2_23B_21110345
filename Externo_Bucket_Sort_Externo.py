import os
import tempfile
import math

# Función para dividir el archivo en bloques
def create_buckets(input_file, num_buckets, buffer_size):
    buckets = [[] for _ in range(num_buckets)]

    with open(input_file, 'rb') as infile:
        while True:
            data = infile.read(buffer_size)
            if not data:
                break
            elements = list(data)
            for element in elements:
                bucket_idx = min(math.floor(element / (256 / num_buckets)), num_buckets - 1)
                buckets[bucket_idx].append(element)
    
    return buckets

# Función para ordenar y escribir los elementos de un bucket en un archivo temporal
def sort_and_write_bucket(bucket, temp_dir):
    bucket.sort()
    with tempfile.NamedTemporaryFile(delete=False, dir=temp_dir) as tmpfile:
        tmpfile.write(bytes(bucket))

# Función principal para Bucket Sort Externo
def bucket_sort_external(input_file, output_file, buffer_size, num_buckets):
    temp_dir = tempfile.mkdtemp()  # Directorio temporal para los archivos temporales
    buckets = create_buckets(input_file, num_buckets, buffer_size)

    for i, bucket in enumerate(buckets):
        if bucket:
            sort_and_write_bucket(bucket, temp_dir)
            buckets[i] = temp_dir + '/' + tmpfile.name

    # Fusionar los archivos temporales en el archivo de salida
    with open(output_file, 'wb') as outfile:
        for bucket_file in buckets:
            with open(bucket_file, 'rb') as infile:
                data = infile.read(buffer_size)
                while data:
                    outfile.write(data)
                    data = infile.read(buffer_size)
            os.remove(bucket_file)

    os.rmdir(temp_dir)  # Eliminar el directorio temporal

# Ejemplo de uso:
if __name__ == "__main__":
    input_file = "input.txt"  # Nombre del archivo de entrada
    output_file = "output.txt"  # Nombre del archivo de salida
    buffer_size = 1000  # Tamaño del buffer en bytes
    num_buckets = 256  # Número de buckets

    bucket_sort_external(input_file, output_file, buffer_size, num_buckets)
    print("Archivo ordenado y guardado en", output_file)
