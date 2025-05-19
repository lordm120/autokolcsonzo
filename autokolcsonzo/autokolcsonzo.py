from berles import Berles

class Autokolcsonzo:
    def __init__(self, nev):
        self.nev = nev
        self.autok = []          
        self.berlesek = []       

    def auto_hozzaadas(self, auto):
        self.autok.append(auto)

    def auto_elérhető(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                return False
        return True

    def berel(self, rendszam, datum, berlo_nev):
        auto = next((a for a in self.autok if a.rendszam == rendszam), None)
        if not auto:
            return f"Nincs ilyen rendszámú autó: {rendszam}"
        if not self.auto_elérhető(rendszam):
            return f"Ez az autó már ki van bérelve: {rendszam}"

        uj_berles = Berles(auto, datum, berlo_nev)
        self.berlesek.append(uj_berles)
        return f"Sikeres bérlés: {auto.rendszam} - {auto.berleti_dij} Ft - Bérlő: {berlo_nev}"

  
    def lemondas(self, rendszam):
        for berles in self.berlesek:
            if berles.auto.rendszam == rendszam:
                self.berlesek.remove(berles)
                return f"Bérlés lemondva: {rendszam}"
        return f"Nincs aktív bérlés ezzel a rendszámmal: {rendszam}"

    def berlesek_listazasa(self):
        if not self.berlesek:
            return "Nincs aktív bérlés."
        return "\n".join(str(berles) for berles in self.berlesek)
    def autok_listazasa(self):
        if not self.autok:
            return "Nincs elérhető autó."
        return "\n".join(str(auto) for auto in self.autok)
