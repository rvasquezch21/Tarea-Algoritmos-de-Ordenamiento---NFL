class punt_play:
    """
    Esta clase representa una jugada de despeje en un partido de fútbol americano.
    """

    # Inicializamos la clase con los atributos de la jugada
    def __init__(self, game_id, teams, yards, qtr):
        self.game_id = game_id
        self.teams = teams
        self.yards = yards
        self.qtr = qtr  

    # Representamos en cadena de la jugada para facilitar su visualización
    def __repr__(self):
        return f"PuntPlay({self.game_id}, {self.teams}, {self.yards}, {self.qtr})"

    # Comparación de jugadas, si tienen el mismo número de yardas
    def __eq__(self, other):
        return self.yards == other.yards

    # Comparación de jugadaa, si una jugada tiene menos yardas que otra
    def __lt__(self, other):
        return self.yards < other.yards

    # Comparación de jugadas, si una jugada tiene más yardas que otra
    def __gt__(self, other):
        return self.yards > other.yards
