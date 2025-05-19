from auto import Auto

class Szemelyauto(Auto):
    def __init__(self, rendszam, tipus, berleti_dij, ulesek_szama):
        super().__init__(rendszam, tipus, berleti_dij)
        self.ulesek_szama = ulesek_szama

    def __str__(self):
        return f"Személyautó - {self.rendszam} ({self.tipus}), {self.ulesek_szama} ülés, {self.berleti_dij} Ft/nap"