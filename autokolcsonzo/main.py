from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from datetime import datetime

def main():
    kolcsonzo = Autokolcsonzo("BestAuto Kölcsönző")

    # 4 autó hozzáadása
    auto1 = Szemelyauto("ABC-123", "Toyota Corolla", 8000, 5)
    auto2 = Teherauto("XYZ-456", "Ford Transit", 12000, 1500)
    auto3 = Szemelyauto("DEF-789", "Honda Civic", 9000, 4)
    auto4 = Szemelyauto("SSD-512", "Bmw e46 M3", 20000, 4)

    kolcsonzo.auto_hozzaadas(auto1)
    kolcsonzo.auto_hozzaadas(auto2)
    kolcsonzo.auto_hozzaadas(auto3)
    kolcsonzo.auto_hozzaadas(auto4)

    # 3 bérlés előre felvétele
    kolcsonzo.berel("ABC-123", "2025-05-18", "Tóth János")
    kolcsonzo.berel("XYZ-456", "2025-05-18", "Kovács József")
    kolcsonzo.berel("DEF-789", "2025-05-19", "Lapos Elemér")

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Kilépés")
        valasztas = input("Válassz egy lehetőséget: ")

        if valasztas == "1":
            rendszam = input("Add meg a rendszámot: ").upper()
            datum = input("Add meg a dátumot (ÉÉÉÉ-HH-NN): ")
            berlo_nev = input("Add meg a neved: ")

            try:
                datetime.strptime(datum, "%Y-%m-%d")
                eredmeny = kolcsonzo.berel(rendszam, datum, berlo_nev)
            except ValueError:
                eredmeny = "Hibás dátumformátum! (pl.: 2025-06-01)"
            print(eredmeny)


        elif valasztas == "2":
            rendszam = input("Add meg a lemondandó autó rendszámát: ").upper()
            print(kolcsonzo.lemondas(rendszam))

        elif valasztas == "3":
            print("\nAktív bérlések:")
            print(kolcsonzo.berlesek_listazasa())

        elif valasztas == "4":
            print("Kilépés...")
            break

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
