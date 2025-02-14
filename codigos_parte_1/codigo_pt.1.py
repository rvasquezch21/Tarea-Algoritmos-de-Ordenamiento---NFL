# IMPORTE DE LIBRERÍAS

from lector_data import DataLector 
from algoritmos import SortingAlgorithms 
import time 
import csv 
import os 

# Definimos una función para guardar los resultados de la ordenación en un archivo CSV
def save_results(filename, plays, start_time, duration, end_time, comparisons, swaps, output_dir):
    # Creamos la carpeta 'resultados'
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)  # Creamos la ruta completa del archivo de resultados

    # Abre el archivo CSV para escribir los resultados
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";") 
        # Titulamos los encabezados de las columnas en los archivos de resultado
        writer.writerow(["start_time", "duracion", "end_time", "comparisons", "swaps", "game_id", "teams", "yards", "qtr"])

        # Escribe cada jugada ordenada junto con los tiempos y estadísticas de comparaciones e intercambios
        for play in plays:
            writer.writerow([f"{start_time:.4f}", f"{duration:.4f}s", f"{end_time:.4f}", comparisons, swaps, play.game_id,
                             play.teams, play.yards, play.qtr])
    print(f"Results saved to {file_path}")  # Confirma que los resultados se guardaron correctamente

# Definimos una función para procesar todos los archivos CSV en un directorio
def process_files_in_directory(directory, output_dir):
    # Listamos todos los archivos CSV en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith(".csv"): 
            file_path = os.path.join(directory, filename)
            print(f"Procesando archivo: {file_path}")
            lector = DataLector(file_path)  # Crea una instancia de DataLector para el archivo
            plays = lector.process_plays()  # Procesa las jugadas del archivo

            # Si no se encontraron jugadas de despeje, sigue con el siguiente archivo
            if not plays:
                print(f"No se encontraron jugadas de despeje en {filename}.")
                continue

            print(f"Total de jugadas de despeje encontradas en {filename}: {len(plays)}\n")

            # Llamamos los algoritmos de ordenación para poder ejecutarlos
            sorting_algorithms = {
                "bubble_sort": SortingAlgorithms.bubble_sort,
                "insertion_sort": SortingAlgorithms.insertion_sort,
                "merge_sort_recursive": SortingAlgorithms.merge_sort_recursive,
                "merge_sort_iterative": SortingAlgorithms.merge_sort_iterative,
                "quick_sort_recursive": SortingAlgorithms.quick_sort_recursive,
                "quick_sort_iterative": SortingAlgorithms.quick_sort_iterative
            }

            # Ejecuta cada algoritmo de ordenación y guarda los resultados
            for name, sort_function in sorting_algorithms.items():
                print(f"Ejecutando {name}...")

                # Medimos el tiempo de comparación
                start_time = time.time()  # Definimos el tiempo de inicio
                sorted_plays, comparisons, swaps, duration = sort_function(plays[:])  # Ordena las jugadas
                end_time = time.time()  # Definimos el tiempo de finalización

                # Muestra estadísticas de tiempo y comparaciones
                print(f"Inicio: {start_time:.4f} | Duración: {duration:.4f}s | Fin: {end_time:.4f}")
                print(f"Comparaciones: {comparisons} | Intercambios: {swaps}\n")

                result_filename = f"primera_parte_{name}_resultado_{filename}"  # Define el nombre del archivo de resultados
                save_results(result_filename, sorted_plays, start_time, duration, end_time, comparisons, swaps, output_dir)  # Guarda los resultados

# Definimos la función principal que ejecuta todo el proceso
if __name__ == "__main__":
    directory = "/Users/rvasquezch21/Documents/Data/primeraprogramada/"  # Ruta del directorio con los archivos CSV
    output_dir = "/Users/rvasquezch21/Documents/Data/resultados/"  # Ruta para guardar los resultados
    process_files_in_directory(directory, output_dir)  # Procesa los archivos en el directorio
