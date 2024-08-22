import random

def prikazi_status(sektor, energija_stita, rakete):
    print(f"\n--- Sektor {sektor}/5 ---")
    print(f"Energija stita: {energija_stita}")
    print(f"Rakete: {rakete}")

def nasumican_broj(min_vrednost, max_vrednost):
    return random.randint(min_vrednost, max_vrednost)

def laserski_napad():
    if nasumican_broj(1, 100) <= 80: #  80% sansu za pogodak
        steta = nasumican_broj(10, 20) # nasumicna steta izmedju 10 i 20
        print(f"Pogodak! Naneli ste {steta} stete neprijatelju")
        return steta
    else:
        print("Promasaj! Niste pogodili neprijatelja!")
        return 0

def ispaliti_raketu(rakete):
    if rakete > 0: # moramo da proverimo da li imamo rakete
        rakete -= 1 # smanjimo broj raketa za jedan
        if nasumican_broj(1, 100) <= 90:
            steta = nasumican_broj(30, 40)
            print(f"Pogodak! Raketa je nanela {steta} stete neprijatelju")
            return steta, rakete
        else:
            print("Promasaj! Raketa nije pogodila neprijatelja")
            return 0, rakete
    else:
        print("Nemate vise raketa!")
        return 0, rakete

def pokusaj_bekstva():
    if nasumican_broj(1, 100) <= 50:
        print("Uspesno ste pobegli!")
        return True
    else:
        print("Bekstvo nije uspelo!")
        return False

def borba_sa_neprijateljem(energija_stita, rakete):
    neprijatelj_hp = 50 # Pocetni HP neprijatelja
    while neprijatelj_hp > 0 and energija_stita > 0:
        print(f"\nHP Neprijatelja: {neprijatelj_hp}")
        print("Izaberite akciju: ")
        print("1. Laserski napad")
        print("2. Ispaliti raketu")
        print("3. Pokusaj Bekstva")

        akcija = input("Unesite broj akcije (1-3): ")

        if akcija == "1":
            neprijatelj_hp -= laserski_napad()
        elif akcija == "2":
            steta, rakete = ispaliti_raketu(rakete)
            neprijatelj_hp -= steta
        elif akcija == "3":
            if pokusaj_bekstva():
                return energija_stita, rakete, False
        else:
            print("Nevazeca akcija. Propustate potez!")

        if neprijatelj_hp <= 0:
            print("Neprijateljski brod je unisten!")
            return energija_stita, rakete, True

        # Neprijatelj vraca udarac!
        if nasumican_broj(1, 100) <= 70:
            steta_neprijatelja = nasumican_broj(10, 15)
            energija_stita -= steta_neprijatelja
            print(f"Neprijatelj vas je pogodio i naneo stetu {steta_neprijatelja} stete! Stanje stita: {energija_stita}")
        else:
            print("Neprijatelj je promasio!")
    return energija_stita, rakete, neprijatelj_hp <= 0

def igraj_svemirski_okrsaj():
    energija_stita = 100 # Pocetna energija stita
    rakete = 3 # Pocetni broj raketa
    unisteni_neprijatelji = 0
    print("comitujem print")

    for sektor in range(1, 6):
        prikazi_status(sektor, energija_stita, rakete)
        # Generisemo nasumican dogadjaj (80% sansa za pojavu neprijatelja)
        if nasumican_broj(1, 100) <= 80:
            print("\nPojavio se neprijateljski brod!")
            energija_stita, rakete, pobeda = borba_sa_neprijateljem(energija_stita, rakete)

            if pobeda:
                unisteni_neprijatelji += 1
        else:
            print("Mirno ste prosli kroz ovaj sektor!")

        if energija_stita <= 0:
            print("Vas stit je unisten! Igra je zavrsena!")
            break

    if energija_stita > 0:
        print("Cestitamo! Preziveli ste svih 5 sektora!")
    else:
        print("\nIgra je zavrsena! Niste uspeli da prezivite 5 sektora!")

    print(f"Unistili ste {unisteni_neprijatelji} neprijateljskih brodova!")



if __name__ == "__main__":
    igraj_svemirski_okrsaj()
