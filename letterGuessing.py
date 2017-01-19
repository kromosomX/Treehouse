import random
import sys


# besede, ki so na voljo za ugibanje


class clear:
    def __call__(self):
        import os
        if os.name == ('ce', 'nt', 'dos'):
            os.system('cls')
        elif os.name == 'posix':
            os.system('clear')
        else:
            print('\n' * 120)

    def __neg__(self):
        self()

    def __repr__(self):
        self();
        return ''


def pisi(zgreseni, zadetki, iskanaBeseda, stevilo_poskusov):
    brisi()
    print("Zgrešil si že {} od {} krat in pri tem vnesel te napačne črke : ".format(len(zgreseni), stevilo_poskusov),
          end="")
    for crka in zgreseni:
        print(crka, end=" ")
    print("\n\n")
    print("Beseda: ", end="")
    for crka in iskanaBeseda:
        if crka in zadetki:
            print(crka, end=" ")
        else:
            print("_", end=" ")
    print("\n\n")


def ugibaj(zgreseni, zadetki):
    while True:
        crka = input("Vsesi crko : ")
        if crka in zadetki or crka in zgreseni:
            print("To črko si že ugibal!")
        elif not (crka.isalpha() or len(crka) != 1):
            print("Vneseš lahko samo črke!")
        else:
            return crka


besede2 = [
    'češnja', 'breskev', 'marelica', 'sliva', 'nektarina',
    'jabolko', 'hruška', 'impkaki', 'kutina', 'nešplja',
    'borovnica', 'grozdje', 'jagoda', 'malina', 'ribez', 'robida', 'brusnica', 'kosmulja',
    'oreh', 'lešnik', 'kostanj', 'arašid', 'mandelj', 'pistacija',
    'limona', 'pomaranča', 'grenivka', 'mandarina', 'limeta',
    'kivi', 'smokva', 'rožič', 'datelj', 'kokos',
    'banana', 'ananas', 'mango', 'papaja', 'avokado'
]
besede = []


def nalozi_seznam():
    global besede
    global besede2
    try:
        datoteka = open("SEZNAMBESED.txt", mode='r', encoding="UTF-8")
        for beseda in datoteka:
            besede.append(beseda.strip())
        datoteka.close()
    except IOError:
        besede = besede2
        datoteka = open("SEZNAMBESED.txt", mode='w', encoding="UTF-8")
        for beseda in besede:
            datoteka.write(beseda + "\n")
        datoteka.close()


def igraj(konec):
    iskanaBeseda = random.choice(besede)  # izbere naključno besedo iz spiska za ugibanje
    stevilo_poskusov = 3 + len(set(iskanaBeseda)) // 2

    zadetki = []
    zgreseni = []
    while True:
        pisi(zgreseni, zadetki, iskanaBeseda, stevilo_poskusov)
        crka = ugibaj(zgreseni, zadetki)
        if crka in iskanaBeseda:
            zadetki.append(crka)
            najdena = True
            for crka in iskanaBeseda:
                if crka not in zadetki:
                    najdena = False
            if najdena:
                print("Zmagal si!")
                print("Iskana beseda je {}".format(iskanaBeseda))
                konec = True
        else:
            zgreseni.append(crka)
            if len(zgreseni) == stevilo_poskusov:
                pisi(zgreseni, zadetki, iskanaBeseda, stevilo_poskusov)
                print("Izgubil si!")
                print("Iskana beseda je {}".format(iskanaBeseda))
                konec = True
        if konec:
            se_enkrat = input("Še ena igra? D/n").lower()
            if se_enkrat != 'n':
                return igraj(konec=False)
            else:
                sys.exit()

    else:
        print("OOPS. Ni ti uspelo v sedmih poskusih")


def dobrodosli():
    start = input("Pritisni 'enter' za začetek ali I za izhod").lower()
    if start == "i":
        print("Adijo!")
        sys.exit()
    else:
        return True


print("Dobrodošli v ugibanju sadja!")
konec = False
brisi = clear()
while True:
    nalozi_seznam()
    brisi()
    dobrodosli()
    igraj(konec)
