from autokolcsonzo import Autokolcsonzo
from szemelyauto import Szemelyauto
from teherauto import Teherauto
from datetime import datetime

def main():
    kolcsonzo = Autokolcsonzo("BestAuto Kölcsönző")

    # 4 autó hozzáadása
    auto1 = Szemelyauto("ADD-329", "Toyota Corolla", 8000, 5)
    auto2 = Teherauto("HKS-756", "Ford Transit", 12000, 1500)
    auto3 = Szemelyauto("LKP-468", "Honda Civic", 9000, 4)
    auto4 = Szemelyauto("SSD-512", "Bmw e46 M3", 20000, 4)

    kolcsonzo.auto_hozzaadas(auto1)
    kolcsonzo.auto_hozzaadas(auto2)
    kolcsonzo.auto_hozzaadas(auto3)
    kolcsonzo.auto_hozzaadas(auto4)

    # 3 bérlés előre felvétele
    kolcsonzo.berel("ADD-329", "2025-05-18", "Tóth János")
    kolcsonzo.berel("HKS-756", "2025-05-18", "Kovács József")
    kolcsonzo.berel("LKP-468", "2025-05-19", "Lapos Elemér")

    while True:
        print("\n--- AUTÓKÖLCSÖNZŐ ---")
        print("1. Autó bérlése")
        print("2. Bérlés lemondása")
        print("3. Bérlések listázása")
        print("4. Autók listázása")
        print("5. Kilépés")

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
            print("Autók listázása")
            print(kolcsonzo.autok_listazasa())
            
        elif valasztas == "5":
            print("Kilépés...")
            break
            

        else:
            print("Érvénytelen választás!")

if __name__ == "__main__":
    main()
