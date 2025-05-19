class Berles:
    def __init__(self, auto, datum, berlo_nev):
        self.auto = auto
        self.datum = datum
        self.berlo_nev = berlo_nev

    def __str__(self):
        return f"{self.berlo_nev} - {self.auto.rendszam} ({self.auto.tipus}) - {self.datum} - {self.auto.berleti_dij} Ft"
