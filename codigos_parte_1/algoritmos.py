# IMPORTE DE LIBRERÍAS

import time

class SortingAlgorithms:
    @staticmethod
    def bubble_sort(arr):
        n = len(arr)  # Obtiene el tamaño de la lista
        comparisons, swaps = 0, 0  # Inicializa contadores de comparaciones e intercambios
        start = time.time()  # Marca el tiempo de inicio

        # Definimos el ordenamiento Bubble Sort: compara elementos adyacentes y los intercambia si están en el orden incorrecto
        for i in range(n):
            for j in range(n - i - 1):
                comparisons += 1  # Incrementa el contador de comparaciones
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Intercambia los elementos
                    swaps += 1  # Incrementa el contador de intercambios

        end = time.time()  # Marca el tiempo de finalización
        return arr, comparisons, swaps, end - start  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración

    @staticmethod
    def insertion_sort(arr):
        comparisons, swaps = 0, 0  # Inicializa contadores
        start = time.time()  # Marca el tiempo de inicio

        # Definimos el ordenamiento por Insertion Sort: coloca cada elemento en la posición correcta
        for i in range(1, len(arr)):
            key = arr[i]  # Toma el elemento actual
            j = i - 1  # Comienza a comparar con el elemento anterior
            while j >= 0 and arr[j] > key:  # Si el elemento es mayor que el "key", lo mueve
                comparisons += 1  # Incrementa el contador de comparaciones
                arr[j + 1] = arr[j]  # Mueve el elemento a la derecha
                swaps += 1  # Incrementa el contador de intercambios
                j -= 1
            arr[j + 1] = key  # Coloca el "key" en su posición correcta

        end = time.time()  # Marca el tiempo de finalización
        return arr, comparisons, swaps, end - start  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración

    @staticmethod
    def merge_sort_iterative(arr):
        start_time = time.time()  # Marca el tiempo de inicio
        comparisons = 0  # Inicializa el contador de comparaciones
        swaps = 0  # Inicializa el contador de intercambios

        width = 1  # Comienza con particiones de tamaño 1
        n = len(arr)  # Obtiene el tamaño del arreglo

        # Definimos el ordenamiento Merge Sort iterativo: fusiona listas de forma iterativa
        while width < n:
            for i in range(0, n, 2 * width):
                left = arr[i:i + width]  # Crea la mitad izquierda
                right = arr[i + width:i + 2 * width]  # Crea la mitad derecha
                merged = []  # Lista vacía para almacenar la fusión
                i_left, i_right = 0, 0  # Índices de las mitades

                while i_left < len(left) and i_right < len(right):
                    comparisons += 1  # Incrementa el contador de comparaciones
                    if left[i_left] < right[i_right]:
                        merged.append(left[i_left])
                        i_left += 1
                    else:
                        merged.append(right[i_right])
                        i_right += 1
                        swaps += 1  # Incrementa el contador de intercambios

                merged.extend(left[i_left:])  # Añade el resto de la izquierda
                merged.extend(right[i_right:])  # Añade el resto de la derecha
                arr[i:i + len(merged)] = merged  # Actualiza el arreglo original

            width *= 2  # Doble el tamaño de las particiones en cada iteración

        end_time = time.time()  # Marca el tiempo de finalización
        return arr, comparisons, swaps, end_time - start_time  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración
 # Definimos el algoritmo de ordenamiento por Merge Sort recursivo
    @staticmethod
    def merge_sort_recursive(arr):
        start_time = time.time()  # Marca el tiempo de inicio
        comparisons = [0]  # Contador de comparaciones
        swaps = [0]  # Contador de intercambios

        # Definimos la función recursiva para realizar el Merge Sort
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  # Encuentra el punto medio
                left_half = arr[:mid]  # Divide el arreglo en la mitad izquierda
                right_half = arr[mid:]  # Divide el arreglo en la mitad derecha

                merge_sort(left_half)  # Llama recursivamente en la mitad izquierda
                merge_sort(right_half)  # Llama recursivamente en la mitad derecha

                i = j = k = 0  # Índices para las mitades
                while i < len(left_half) and j < len(right_half):  # Compara los elementos de las mitades
                    comparisons[0] += 1  # Cuenta las comparaciones
                    if left_half[i] < right_half[j]:  # Si el elemento de la izquierda es menor, se coloca en el arreglo ordenado
                        arr[k] = left_half[i]
                        i += 1
                    else:  # Si el elemento de la derecha es menor, se coloca en el arreglo ordenado
                        arr[k] = right_half[j]
                        j += 1
                        swaps[0] += 1  # Cuenta los intercambios
                    k += 1

                # Añade los elementos restantes de la mitad izquierda
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                # Añade los elementos restantes de la mitad derecha
                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(arr)  # Llama a la función recursiva para ordenar el arreglo

        end_time = time.time()  # Marca el tiempo de finalización
        return arr, comparisons[0], swaps[0], end_time - start_time  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración

 # Definimos el algoritmo ordenamiento por Merge Sort recursivo
    @staticmethod
    def merge_sort_recursive(arr):
        start_time = time.time()  # Marca el tiempo de inicio
        comparisons = [0]  # Contador de comparaciones
        swaps = [0]  # Contador de intercambios

        # Definimos una función recursiva para realizar la ordenación por mezcla
        def merge_sort(arr):
            if len(arr) > 1:
                mid = len(arr) // 2  # Encuentra el punto medio
                left_half = arr[:mid]  # Divide el arreglo en la mitad izquierda
                right_half = arr[mid:]  # Divide el arreglo en la mitad derecha

                merge_sort(left_half)  # Llama recursivamente en la mitad izquierda
                merge_sort(right_half)  # Llama recursivamente en la mitad derecha

                i = j = k = 0  # Índices para las mitades
                while i < len(left_half) and j < len(right_half):  # Compara los elementos de las mitades
                    comparisons[0] += 1 
                    if left_half[i] < right_half[j]:  # Si el elemento de la izquierda es menor, se coloca en el arreglo ordenado
                        arr[k] = left_half[i]
                        i += 1
                    else:  # Si el elemento de la derecha es menor, se coloca en el arreglo ordenado
                        arr[k] = right_half[j]
                        j += 1
                        swaps[0] += 1
                    k += 1

                # Añade los elementos restantes de la mitad izquierda
                while i < len(left_half):
                    arr[k] = left_half[i]
                    i += 1
                    k += 1

                # Añade los elementos restantes de la mitad derecha
                while j < len(right_half):
                    arr[k] = right_half[j]
                    j += 1
                    k += 1

        merge_sort(arr)  # Llama a la función recursiva para ordenar el arreglo

        end_time = time.time()  # Marca el tiempo de finalización
        return arr, comparisons[0], swaps[0], end_time - start_time  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración

# Definimos el algoritmos de ordenamiento Quick Sort recursivo
    @staticmethod
    def quick_sort_recursive(arr):
        start_time = time.time()  # Marca el tiempo de inicio
        comparisons = [0]  # Contador de comparaciones
        swaps = [0]  # Contador de intercambios

        # Función recursiva para realizar la ordenación rápida
        def quick_sort(arr):
            if len(arr) <= 1:  # Si el arreglo tiene un solo elemento, ya está ordenado
                return arr

            pivot = arr[len(arr) // 2]  # Toma el elemento central como pivote
            left = []  # Lista para elementos menores que el pivote
            middle = []  # Lista para los elementos iguales al pivote
            right = []  # Lista para elementos mayores que el pivote

            # Compara cada elemento con el pivote
            for play in arr:
                comparisons[0] += 1 
                if play < pivot:  # Si el elemento es menor que el pivote, se agrega a la lista izquierda
                    left.append(play)
                elif play > pivot:  # Si el elemento es mayor que el pivote, se agrega a la lista derecha
                    right.append(play)
                    swaps[0] += 1
                else:  # Si el elemento es igual al pivote, se agrega a la lista central
                    middle.append(play)

            # Ordena las listas recursivamente y las combina
            return quick_sort(left) + middle + quick_sort(right)

        sorted_arr = quick_sort(arr)  # Llama a la función recursiva para ordenar el arreglo
        end_time = time.time()  # Marca el tiempo de finalización
        return sorted_arr, comparisons[0], swaps[0], end_time - start_time  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración

# Definimos el algoritmo de Quick Sort iterativo
    @staticmethod
    def quick_sort_iterative(arr):
        start_time = time.time()  # Marca el tiempo de inicio
        comparisons = 0  # Inicializa el contador de comparaciones
        swaps = 0  # Inicializa el contador de intercambios

        stack = [(0, len(arr) - 1)]  # Pila para almacenar los índices de los subarreglos a ordenar

        # Recorre los subarreglos de manera iterativa utilizando una pila
        while stack:
            left, right = stack.pop()  # Saca el siguiente subarreglo de la pila
            if left >= right:  # Si el subarreglo tiene un solo elemento, ya está ordenado
                continue

            pivot_index = (left + right) // 2  # Elige el pivote
            pivot = arr[pivot_index]  # Toma el valor del pivote
            i, j = left, right  # Inicializa los índices

            # Reorganiza los elementos alrededor del pivote
            while i <= j:
                while arr[i] < pivot:  # Mueve los elementos menores que el pivote hacia la izquierda
                    comparisons += 1
                    i += 1
                while arr[j] > pivot:  # Mueve los elementos mayores que el pivote hacia la derecha
                    comparisons += 1
                    j -= 1
                if i <= j:  # Si los índices no se cruzan, intercambia los elementos
                    arr[i], arr[j] = arr[j], arr[i]
                    swaps += 1  # Cuenta los intercambios
                    i += 1
                    j -= 1

            # Agrega los subarreglos a la pila para procesarlos
            if left < j:
                stack.append((left, j))
            if i < right:
                stack.append((i, right))

        end_time = time.time()  # Marca el tiempo de finalización
        return arr, comparisons, swaps, end_time - start_time  # Devuelve el arreglo ordenado, comparaciones, intercambios y duración

# Función para realizar la partición en el algoritmo de ordenamiento rápido
    @staticmethod
    def partition(arr, low, high):
        pivot = arr[high]  # Elige el último elemento como pivote
        i = low - 1  # Inicializa el índice para realizar la partición

        for j in range(low, high):
            if arr[j] < pivot:  # Si el elemento es menor que el pivote, se mueve a la izquierda
                i += 1
                arr[i], arr[j] = arr[j], arr[i]  # Intercambia los elementos

        arr[i + 1], arr[high] = arr[high], arr[i + 1]  # Coloca el pivote en su posición correcta
        return i + 1  # Devuelve el índice del pivote