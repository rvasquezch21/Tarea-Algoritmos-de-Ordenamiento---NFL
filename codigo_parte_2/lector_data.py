# IMPORTE DE LIBRERÍAS

import csv 
import os 
from clase_punt import punt_play 
from comparator import play_comparator 

# Definimos la clase para poder leer las jugadas de la NFL dentro de los archivos
class DataLector:
    def __init__(self, filename):
        self.filename = filename

    # Definimos una función para procesar las jugadas en el archivo CSV
    def process_plays(self):
        # Verifica si el archivo existe
        if not os.path.exists(self.filename):
            print(f"Error de carga: El archivo {self.filename} no existe.")
            return []

        plays = []  # Definimos una lista donde se guardarán las jugadas de despeje

        try:
            # Abre el archivo CSV para lectura y lo lee línea por línea
            with open(self.filename, "r", encoding="utf-8") as file:
                reader = csv.reader(file)  # Lee el archivo como un lector CSV
                header = next(reader)  # Lee la primera línea como el encabezado
                print(f"Archivo cargado correctamente: {self.filename}")
                print("Encabezado del archivo CSV:", header)

                # Definimos los índices de las columnas que nos interesan
                DESC_IDX = 19
                DATE_IDX = 0
                GAME_ID_IDX = 1
                POSTEAM_IDX = 17
                DEFTEAM_IDX = 18
                QTR_IDX = 4
                YARDS_IDX = 21
                TIME_IDX = 7
                
                comparator = play_comparator()  # Creamos una instancia de play_comparator para ordenar las jugadas

                # Recorremos cada línea del archivo CSV
                for i, data in enumerate(reader):

                    # Si los datos en la línea son incompletos, los saltamos
                    if len(data) <= max(DESC_IDX, DATE_IDX, GAME_ID_IDX, POSTEAM_IDX, DEFTEAM_IDX, QTR_IDX, YARDS_IDX, TIME_IDX):
                        print(f"Saltando línea {i + 1}: datos incompletos → {data}")
                        continue

                    # Extraemos y procesamos la descripción de la jugada
                    description = data[DESC_IDX].strip('"').lower()

                    if i < 5:
                        print(f"Descripción {i + 1}: {description}")

                    # Solo procesamos jugadas de "punt" que no sean "fumble"
                    if "punt" in description and "fumble" not in description:
                        # Extraemos el ID del juego y los equipos involucrados
                        game_id = data[GAME_ID_IDX]
                        teams = f"{data[POSTEAM_IDX]}@{data[DEFTEAM_IDX]}"

                        # Intentamos extraer las yardas, cuarto, fecha y hora
                        try:
                            yards = int(float(data[YARDS_IDX]))
                            qtr = int(data[QTR_IDX])
                            date = data[DATE_IDX]
                            time = data[TIME_IDX]
                        except ValueError:
                            # Si hay un error al convertir los datos, saltamos esta línea
                            print(f"Saltando línea {i + 1} por datos inválidos en Yards o Qtr: {data[YARDS_IDX]}, {data[QTR_IDX]}")
                            continue

                        # Creamos una instancia de punt_play y la agregamos a la lista de jugadas
                        play = punt_play(game_id, teams, yards, qtr, date, time)
                        plays.append(play)

                # Mostramos cuántas jugadas de despeje se encontraron
                print(f"Jugadas de despeje encontradas: {len(plays)}")

                # Ordenamos las jugadas usando el comparador definido anteriormente
                plays.sort(key=lambda play: comparator.compare(play, play))  # Ordenamos usando el comparador
                print("Jugadas ordenadas correctamente.")
                
        except Exception as e:
            # Si hubo algún error leyendo el archivo, lo mostramos
            print(f"ERROR al leer el archivo: {e}")
            return []

        return plays  # Devolvemos la lista de jugadas procesadas
