class punt_play:
    def __init__(self, game_id, teams, yards, quarter, date, time):
        """
        Esta funcion inicializa una jugada de tipo "punt".
        """
        self.game_id = game_id 
        self.teams = teams 
        self.yards = yards 
        self.quarter = quarter
        self.date = date
        self.time = time 

    def __eq__(self, other):
        """
        Compara si dos jugadas son iguales (comparando yardas y otros atributos si es necesario)
        """
        return (self.date == other.date and  # Compara por fecha
                self.quarter == other.quarter and  # Compara por cuarto
                self.yards == other.yards and  # Compara por yardas
                self.time == other.time)  # Compara por hora

    def __gt__(self, other):
        """
        Compara si esta jugada es "mayor" que otra, basándose en los criterios de la fecha, cuarto,
        yardas y hora.
        """
        if self.date > other.date:  # Compara por fecha
            return True
        elif self.date < other.date:
            return False
        
        if self.quarter > other.quarter:  # Compara por cuarto
            return True
        elif self.quarter < other.quarter:
            return False
        
        if self.yards > other.yards:  # Compara por yardas
            return True
        elif self.yards < other.yards:
            return False
        
        return self.time > other.time  # Compara por tiempo

    def __lt__(self, other):
        """
        Compara si esta jugada es "menor" que otra, basándose en los mismos criterios que en __gt__.
        """
        if self.date < other.date:  # Compara por fecha
            return True
        elif self.date > other.date:
            return False
        
        if self.quarter < other.quarter:  # Compara por cuarto
            return True
        elif self.quarter > other.quarter:
            return False
        
        if self.yards < other.yards:  # Compara por yardas
            return True
        elif self.yards > other.yards:
            return False
        
        return self.time < other.time  # Compara por tiempo

