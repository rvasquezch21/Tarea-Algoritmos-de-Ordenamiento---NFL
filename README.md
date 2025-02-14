# README --- Tarea Programada 1: Ordenación de Jugadas en Python
Introducción
    Este proyecto tiene como objetivo ordenar las jugadas de fútbol americano obtenidas de un archivo CSV, específicamente jugadas de tipo "punt", 
    utilizando diferentes algoritmos de ordenación. El código está basado en la programación orientada a objetos, 
    con el uso de clases personalizadas y sobrescritura de métodos especiales en Python.

Descripción del Proyecto
    El proyecto se divide en dos partes principales:

Primera Parte
    Clase punt_play: Se crea una clase que representa una jugada de tipo "punt". 
        Esta clase tiene los siguientes atributos:
            id del juego: Identificador del partido.
            equipos: Representado como un string con las abreviaturas de los equipos, en formato "equipo visitante@equipo casa".
            yardas: Distancia ganada en la jugada.
            cuarto: Cuarto en el que ocurrió la jugada.

    Clase lector_data: Esta clase se encarga de leer un archivo CSV, filtrar las jugadas de tipo "punt" (sin fumbles), 
        y devolver una lista con las jugadas filtradas. Además, se implementan los métodos de comparación __eq__, __lt__, y __gt__ 
        en la clase punt_play para poder ordenar los objetos basados en la cantidad de yardas.

    Algoritmos de Ordenación: Se implementan los algoritmos de ordenación:
        Bubble Sort
        Insertion Sort
        Merge Sort (tanto iterativo como recursivo)
        Quick Sort (tanto iterativo como recursivo)

    Los algoritmos deben ser modificados para comparar objetos punt_play sin acceder directamente a sus atributos, 
    utilizando los operadores de comparación definidos en los métodos sobrescritos.

Generación de Archivos: El código debe generar archivos CSV con las jugadas ordenadas por cada algoritmo. 
Los resultados deben incluir estadísticas de tiempo y comparaciones realizadas durante el proceso de ordenación.

Segunda Parte
    Modificación de la Comparación: En esta parte, la comparación de jugadas se realiza utilizando una nueva clase llamada play_comparator. 
    Esta clase tiene un método compare() que compara las jugadas siguiendo los criterios:

        Fecha de la jugada (de la más antigua a la más reciente)
        Cuarto del partido
        Yardas ganadas
        Tiempo de la jugada (en caso de empate en yardas)
    Implementación de Algoritmos: Los mismos algoritmos de ordenación se utilizan, 
    pero ahora se implementan con el play_comparator para ordenar las jugadas según los nuevos criterios.

Archivos de Salida: Se generan nuevos archivos CSV que contienen las jugadas ordenadas según los criterios de la segunda parte, 
sin estadísticas de comparaciones o intercambios.


Funcionalidad del Programa
    Lectura de Archivos: El programa lee los archivos CSV de jugadas de la temporada de la NFL, 
        filtrando solo las jugadas de tipo "punt" que no contienen "fumble".

    Ordenación de Jugadas: Utiliza los algoritmos de ordenación mencionados anteriormente para ordenar las jugadas por yardas en la primera parte 
        y por los criterios definidos en la segunda parte (fecha, cuarto, yardas, tiempo).

    Generación de Resultados: El programa genera archivos CSV con las jugadas ordenadas 
        y muestra en pantalla las estadísticas de tiempo de ejecución de cada algoritmo.

    Salida de Datos: Los resultados son guardados en archivos con nombres que incluyen el nombre del algoritmo de ordenación 
        y la parte correspondiente del trabajo.
