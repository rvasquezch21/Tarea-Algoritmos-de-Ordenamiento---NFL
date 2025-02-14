class play_comparator:
    def compare(self, play_a, play_b):
        # Compara primero por la fecha
        if play_a.date < play_b.date:
            return -1
        elif play_a.date > play_b.date:
            return 1
        
        # Si las fechas son iguales, compara por el cuarto
        if play_a.quarter < play_b.quarter:
            return -1
        elif play_a.quarter > play_b.quarter:
            return 1
        
        # Si los cuartos son iguales, compara por yardas
        if play_a.yards < play_b.yards:
            return -1
        elif play_a.yards > play_b.yards:
            return 1
        
        # Si las yardas son iguales, compara por el tiempo
        if play_a.time < play_b.time:
            return -1
        elif play_a.time > play_b.time:
            return 1
        
        # Si todo es igual, son iguales
        return 0
