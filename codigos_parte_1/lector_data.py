# IMPORTE DE LIBRERÍAS

import csv 
import os 
from clase_punt import punt_play

# Definimos una clase para poder leer los datos de las jugadas de la NFL de los archivos
class DataLector:
    # Inicializamos el objeto DataLector con el nombre de un archivo
    def __init__(self, filename):
        self.filename = filename

    # Procesamos las jugadas contenidas en el archivo CSV
    def process_plays(self):
        # Definimos una funcion que verifica si el archivo existe
        if not os.path.exists(self.filename):
            print(f"Error de carga: El archivo {self.filename} no existe.")
            return []

        plays = []  # Lista para almacenar las jugadas de despeje

        try:
            # Abre el archivo CSV para leerlo
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)  # Creamos un lector de CSV
                header = next(reader)  # Leemos el encabezado del archivo
                print(f"Archivo cargado correctamente: {self.filename}")
                print("Encabezado del archivo CSV:", header)

                # Índices de las columnas en el archivo CSV que contienen los datos relevantes
                DESC_IDX = 19
                GAME_ID_IDX = 1
                POSTEAM_IDX = 17
                DEFTEAM_IDX = 18
                YARDS_IDX = 21
                QTR_IDX = 4

                # Recorremos las líneas del archivo CSV, saltando las que no contienen todos los datos necesarios
                for i, data in enumerate(reader):
                    # Si los datos están incompletos, se salta la línea
                    if len(data) <= max(DESC_IDX, GAME_ID_IDX, POSTEAM_IDX, DEFTEAM_IDX, YARDS_IDX, QTR_IDX):
                        print(f"Saltando línea {i + 1}: datos incompletos → {data}")
                        continue

                    # Extraemos y procesamos la descripción de la jugada
                    description = data[DESC_IDX].strip('"').lower()

                    # Mostramos las primeras 5 descripciones
                    if i < 5:
                        print(f"Descripción {i + 1}: {description}")

                    # Procesamos solo jugadas de "punt" que no sean "fumble"
                    if "punt" in description and "fumble" not in description:
                        # Extraemos el ID del juego y los equipos involucrados
                        game_id = data[GAME_ID_IDX]
                        teams = f"{data[POSTEAM_IDX]}@{data[DEFTEAM_IDX]}"

                        # Intentamos extraer las yardas y el cuarto del juego
                        try:
                            yards = int(float(data[YARDS_IDX]))
                            qtr = int(data[QTR_IDX])
                        except ValueError:
                            # Si hay un error con los valores de yardas o cuarto, se salta la línea
                            print(f"Saltando línea {i + 1} por datos inválidos en Yards o Qtr: {data[YARDS_IDX]}, {data[QTR_IDX]}")
                            continue

                        # Creamos una instancia de la clase punt_play y la agrega a la lista de jugadas
                        plays.append(punt_play(game_id, teams, yards, qtr))

                # Mostramos la cantidad de jugadas de despeje encontradas
                print(f"Jugadas de despeje encontradas: {len(plays)}")
        except Exception as e:
            # Si hubo algún error leyendo el archivo, lo muestra
            print(f"ERROR al leer el archivo: {e}")
            return []

        return plays  # Devuelve la lista de jugadas procesadas