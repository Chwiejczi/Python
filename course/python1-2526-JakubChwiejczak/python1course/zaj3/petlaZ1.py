import math
import random

##---------------zadanie1
imiona = ["Anna", "Jan", "Ewa"]
oceny = [5, 4, 3]

for imie, ocena in zip(imiona, oceny):
    print(f"{imie} ma ocenę {ocena}")


#######-----------------------------zadanie 2

liczba = random.randint(1, 100)
for proba in range(100):
    odp = int(input("Podaj liczbę: "))
    if odp == liczba:
        print(f"zgadnieta liczba:{liczba}, zagadnieta za{proba} razem")
        break
    elif odp > liczba:
        print("za duzo")
    elif odp < liczba:
        print("za malo")


# ---------------------------zadanie 3
trojkaty = [(3, 4, 5), (5, 12, 13), (7, 8, 9), (8, 15, 17)]
for i, tr in enumerate(trojkaty):
    print(f"ix:{i}, trojkat{tr}")
    a, b, c = tr
    p = (a + b + c) / 2
    S = math.sqrt(p * (p - a) * (p - b) * (p - c))
    print(f"Pole nr {i} wynosi {S}")
    if tr[0] ** 2 + tr[1] ** 2 == tr[2] ** 2:
        print("trojkat jest prostokatny")
