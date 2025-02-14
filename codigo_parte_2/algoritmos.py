class SortingAlgorithms:
    @staticmethod
    def bubble_sort(plays, comparator):
        n = len(plays)  # Obtenemos la longitud de la lista de jugadas

        for i in range(n):  # Recorremos todas las jugadas
            for j in range(n - i - 1):  # Recorremos las jugadas de forma que las últimas queden ordenadas
                if comparator.compare(plays[j], plays[j + 1]) > 0:  # Comparamos las jugadas usando un comparador
                    plays[j], plays[j + 1] = plays[j + 1], plays[j]  # Intercambiamos las jugadas

        return plays  # Devolvemos el resultado de la lista ordenada

    @staticmethod
    def insertion_sort(plays, comparator):

        for i in range(1, len(plays)):  # Comenzamos con la segunda jugada y la insertamos correctamente en su lugar
            key = plays[i]  # Definimos la jugada a insertar
            j = i - 1  # Buscamos la posición correcta hacia atrás
            while j >= 0 and comparator.compare(plays[j], key) > 0:  # Comparamos y desplazamos las jugadas mayores
                plays[j + 1] = plays[j]  # Desplazamos las jugadas
                j -= 1  # Continuamos buscando la posición adecuada
            plays[j + 1] = key  # Colocamos la jugada en la posición correcta

        return plays  # Devolvemos el resultado

    @staticmethod
    def merge_sort_iterative(plays, comparator):
        width = 1  # Comenzamos con un ancho de partición de 1
        n = len(plays)  # Obtenemos el tamaño de la lista de jugadas

        while width < n:  # Repetimos mientras el ancho sea menor que el tamaño de la lista
            for i in range(0, n, 2 * width):  # Recorremos la lista en pasos de 2 * width
                left = plays[i:i + width]  # Separamos la lista en dos mitades
                right = plays[i + width:i + 2 * width]
                merged = []  # Lista para almacenar las jugadas fusionadas
                i_left, i_right = 0, 0  # Índices para las mitades

                while i_left < len(left) and i_right < len(right):  # Comparamos las jugadas en ambas mitades
                    if comparator.compare(left[i_left], right[i_right]) < 0:
                        merged.append(left[i_left])
                        i_left += 1
                    else:
                        merged.append(right[i_right])
                        i_right += 1

                merged.extend(left[i_left:])  # Agregamos las jugadas restantes
                merged.extend(right[i_right:])
                plays[i:i + len(merged)] = merged  # Actualizamos la lista original con las jugadas fusionadas

            width *= 2  # Doblamos el tamaño del ancho para la siguiente iteración

        return plays  # Devolvemos el resultado

    @staticmethod
    def merge_sort_recursive(plays, comparator):

        def merge_sort(plays):  # Función recursiva para ordenar
            if len(plays) > 1: 
                mid = len(plays) // 2  # Encontramos el punto medio
                left_half = plays[:mid]  # Dividimos la lista
                right_half = plays[mid:]

                merge_sort(left_half)  # Ordenamos recursivamente la mitad izquierda
                merge_sort(right_half)  # Ordenamos recursivamente la mitad derecha

                i = j = k = 0  # Índices para las mitades
                while i < len(left_half) and j < len(right_half):  # Comparamos las jugadas de las mitades
                    if comparator.compare(left_half[i], right_half[j]) < 0:
                        plays[k] = left_half[i]
                        i += 1
                    else:
                        plays[k] = right_half[j]
                        j += 1
                    k += 1

                while i < len(left_half):  # Agregamos las jugadas restantes de la mitad izquierda
                    plays[k] = left_half[i]
                    i += 1
                    k += 1

                while j < len(right_half):  # Agregamos las jugadas restantes de la mitad derecha
                    plays[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(plays)  # Llamamos a la función recursiva para ordenar las jugadas

        return plays  # Devolvemos el resultado

    @staticmethod
    def quick_sort_recursive(plays, comparator):

        def quick_sort(plays):  # Función recursiva para quick sort
            if len(plays) <= 1:  # Si hay 0 o 1 jugada, ya está ordenada
                return plays

            pivot = plays[len(plays) // 2]  # Elegimos el pivote
            left = []  # Lista de jugadas menores al pivote
            middle = []  # Lista de jugadas iguales al pivote
            right = []  # Lista de jugadas mayores al pivote

            for play in plays:  # Comparamos las jugadas con el pivote
                if comparator.compare(play, pivot) < 0:
                    left.append(play)
                elif comparator.compare(play, pivot) > 0:
                    right.append(play)
                else:
                    middle.append(play)

            return quick_sort(left) + middle + quick_sort(right)  # Ordenamos las listas recursivamente

        sorted_arr = quick_sort(plays)  # Llamamos a la función para ordenar las jugadas
        return sorted_arr  # Devolvemos el resultado

    @staticmethod
    def quick_sort_iterative(plays, comparator):
        stack = [(0, len(plays) - 1)]  # Pila para almacenar los índices a procesar

        while stack:  # Mientras haya elementos en la pila
            left, right = stack.pop()  # Sacamos el siguiente rango de la pila
            if left >= right:  # Si ya está ordenado, continuamos
                continue

            pivot_index = (left + right) // 2  # Elegimos el pivote
            pivot = plays[pivot_index]
            i, j = left, right

            while i <= j:  # Reordenamos la lista basándonos en el pivote
                while comparator.compare(plays[i], pivot) < 0:  # Buscamos un valor mayor al pivote
                    i += 1
                while comparator.compare(plays[j], pivot) > 0:  # Buscamos un valor menor al pivote
                    j -= 1
                if i <= j:
                    plays[i], plays[j] = plays[j], plays[i]  # Intercambiamos las jugadas
                    i += 1
                    j -= 1

            if left < j:  # Si es necesario, agregamos más rangos a la pila
                stack.append((left, j))
            if i < right:
                stack.append((i, right))

        return plays # Devolvemos el resultado

