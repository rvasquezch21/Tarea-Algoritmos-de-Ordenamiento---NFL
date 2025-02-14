# IMPORTE DE LIBRERÍAS

import csv
import os
from lector_data import DataLector
from algoritmos import SortingAlgorithms
from comparator import play_comparator  # Importar el comparador

# Definimos una función para guardar los resultados en un archivo CSV
def save_results(filename, plays, output_dir):
    # Creamos el directorio de resultados si no existe
    os.makedirs(output_dir, exist_ok=True)

    file_path = os.path.join(output_dir, filename)  # Crea la ruta completa para el archivo de salida

    # Abre el archivo para escritura y guarda las jugadas ordenadas
    with open(file_path, "w", encoding="utf-8", newline="") as file:
        writer = csv.writer(file, delimiter=";")
        writer.writerow(["game_id", "teams", "date", "qtr", "yards", "time"])  # Titulamos el encabezado de las columnas

        # Escribimos cada jugada en una fila del archivo CSV
        for play in plays:
            writer.writerow([play.game_id, play.teams, play.date, play.quarter, play.yards, play.time])
    print(f"Results saved to {file_path}")  # Confirmamos que los resultados se guardaron correctamente


# Definimos una función para procesar todos los archivos CSV en un directorio
def process_files_in_directory(directory, output_dir):
    # Lista todos los archivos CSV en el directorio especificado
    for filename in os.listdir(directory):
        if filename.endswith(".csv"): 
            file_path = os.path.join(directory, filename) 
            print(f"Procesando archivo: {file_path}")
            lector = DataLector(file_path)  # Creamos una instancia de DataLector para este archivo
            plays = lector.process_plays()  # Procesamos las jugadas

            # Si no se encontraron jugadas, seguimos con el siguiente archivo
            if not plays:
                print(f"No se encontraron jugadas de despeje en {filename}.")
                continue

            print(f"Total de jugadas de despeje encontradas en {filename}: {len(plays)}\n")

            # Creamos una instancia de play_comparator para usar en los algoritmos de ordenación
            comparator = play_comparator()

            # Diccionario de los diferentes algoritmos de ordenación a utilizar
            sorting_algorithms = {
                "bubble_sort": SortingAlgorithms.bubble_sort,
                "insertion_sort": SortingAlgorithms.insertion_sort,
                "merge_sort_recursive": SortingAlgorithms.merge_sort_recursive,
                "merge_sort_iterative": SortingAlgorithms.merge_sort_iterative,
                "quick_sort_recursive": SortingAlgorithms.quick_sort_recursive,
                "quick_sort_iterative": SortingAlgorithms.quick_sort_iterative
            }

            # Ejecutamos cada algoritmo de ordenación y guardamos los resultados
            for name, sort_function in sorting_algorithms.items():
                print(f"Ejecutando {name}...")

                # Usamos el comparador en el algoritmo de ordenación para ordenar las jugadas
                sorted_plays = sort_function(plays[:], comparator)  # Pasamos una copia de plays
                result_filename = f"segunda_parte_{name}_resultado_{filename}"  # Definimos el nombre del archivo de resultados
                save_results(result_filename, sorted_plays, output_dir)  # Guardamos los resultados en un archivo CSV


# Función principal que ejecuta todo el proceso
if __name__ == "__main__":
    directory = "/Users/rvasquezch21/Documents/Data/primeraprogramada/"  # Ruta del directorio de entrada
    output_dir = "/Users/rvasquezch21/Documents/Data/resultados/"  # Ruta del directorio de salida
    process_files_in_directory(directory, output_dir)  # Procesamos los archivos en el directorio
