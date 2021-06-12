#Python 3.9 Kamień, Papier i Nożyce

import random

print("\nWitaj w grze Kamień, papier i nożyce\n")
while True:
    użytkownik = input("Wybierz - kamień, papier, czy nożyce: ")
    wybór = ["kamień", "papier", "nożyce"]
    komputer = random.choice(wybór)
    print(f"\nTwój wybór {użytkownik}, komputer wybrał {komputer}.\n")

    if użytkownik == komputer:
        print(f"Uzytkownik wybrał: {użytkownik} i komputer wybrał: {komputer}. Remis!!!")
    elif użytkownik == "kamień":
        if komputer == "nożyczki":
            print("Kamień pokonuje nożyczki! Wygrałeś!!!")
        else:
            print("Papier zostaje pokonany przez nożyczki! Przegrałeś!!!")
    elif użytkownik == "papier":
        if komputer == "kamień":
            print("Papier owija kamień! Wygrałeś!!!")
        else:
            print("Nozyczki tną papier. Przegrałeś!!!")
    elif użytkownik == "nożyczki":
        if komputer == "papier":
            print("Nożyczki tną papier. Wygrałeś!!!")
        else:
            print("Kamień tępi nożyczki. Przegrałeś!!!")

    zagraj_jeszcze_raz = input("Grasz jeszcze raz? (y/n): ")
    if zagraj_jeszcze_raz.lower() !="y":
        break