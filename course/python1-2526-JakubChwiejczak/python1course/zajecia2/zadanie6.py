a, b, c = [1, 2, 3]

skladniki = ["mąka", "jajka", "mleko", "cukier", "sól"]
baza, *glowne_skladniki, przyprawy = skladniki
print(f"Baza przepisu to {baza}")
print(f"Główne składniki to {glowne_skladniki}")
print(f"A {przyprawy} to użyte przyprawy.")


dane = (2024, "Python", 3.8)
rok, jezyk, wersja = dane

oceny = [4, 3, 5, 2, 5, 4]
pierwsza, *srodek, ostatnia = oceny


info = ("Jan", "Kowalski", 30, "Polska", "programista")
imie, nazwisko, _, _, zawod = info

dane = (2024, ["Python", 3.8, ("Stabilna", "Wersja")])
rok, [jezyk, wersja, (opis, _)] = dane


a = b = [1, 2, 3]
b[0] = "zmieniono"
print(a, b)  # b wplynelo na a, poniewaz osdosza sie do tego samego miejsca w pamieci


c = list(a)


c[
    0
] = "nowa wartość"  # bo przy inicjowaniu zminnej co 'rezerwujemy ' nowe miejsce w pamieci


print(f"Lista a: {a}, lista b: {b}, lista c: {c}")

x = y = 10
y = y + 1  # y teraz wskazuje na nowy obiekt w innym miejscu w pamieci
print(f"x: {x}, y: {y}")


K = [1, 2]
L = K
# konkatenacja
K = K + [3, 4]
M = [1, 2]
N = M
# przypisanie rozszerzone
M += [3, 4]
