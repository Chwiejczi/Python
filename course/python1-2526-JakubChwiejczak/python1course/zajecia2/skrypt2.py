import math
from random import choice

wartosc = 100
dodawanie = wartosc + 123.15
potega = dodawanie**12
tekst = str(potega)
wartosc_pi = math.pi
lis = [1, 2, 3, 4, 5]
losowa = choice(lis)
# print(losowa)

tekst = f"Wartosc: {tekst}"
print(len(tekst))
print(tekst[1:4])
# print(dir(tekst))
tekst = tekst.upper()
# tekst[2]="p"


lista = list(tekst)
lista = lista[:8]
print(lista)
lista.append(choice(lis))
lista.remove(":")
print(lista)

lista2 = [1, 2, 3, "banan", 100]
lista3 = [x if x == "banan" else x**2 for x in lista2]
print(lista3)

lista4 = list(range(2, 18, 2))
print(lista4)


ja = {}
ja["imie"] = "Jakub"
ja["nazwisko"] = "Chwiejczak"
ja["wiek"] = 20
ja["hobby"] = "sport"
print(ja["hobby"])
print(ja)
ad = "adres" in ja
print(ad)


krotka1 = (1, 2, "3", 4, 2, 5)
print(f"{krotka1[0]}, dlugosc:{len(krotka1)}")
ile = krotka1.count(2)
print(ile)


X = set("kalarepa")
Y = set("lepy")

print(X & Y)
