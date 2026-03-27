def zmien_wartosc(arg):
    if isinstance(arg, list):
        arg[0] = "kalafior"
    elif isinstance(arg, int):
        arg = 65482652
    return arg


lista = [1, 2, 3]
print("Przed:", lista)
zmien_wartosc(lista)
print("Po:   ", lista)
liczba = 10
print("\nPrzed:", liczba)
zmien_wartosc(liczba)
print("Po:   ", liczba)


# dodanie wartości domyślnych
def dodaj(a=0, b=0):
    return a + b


# argumenty pozycyjne przekazywane są w podanej kolejności
print(dodaj(3, 5))


# =====================
def zamowienie_produktu(nazwa_produktu, *, cena, ilosc=1):
    cal = cena * ilosc
    return f"{nazwa_produktu}, laczna cena {cal}, ilosc{ilosc}", cal


lista = [
    zamowienie_produktu("a", cena=2, ilosc=3),
    zamowienie_produktu("a", cena=3, ilosc=4),
    zamowienie_produktu("c", cena=1, ilosc=3),
]

for i in lista:
    print(i)


# ======================
def oblicz_srednia_ocen(*args, wagi=None):
    if wagi == None:
        return sum(args) / len(args)
    else:
        sumaWag = 0
        sumaWazona = 0
        for i in args:
            waga = wagi.get(i)
            sumaWag = sumaWag + waga
            sumaWazona = sumaWazona + i * waga
        return sumaWazona / sumaWag


# -----------------------------
def polynomial_calculator(x, *wspolczynniki, **opcjonalne):
    dl = len(wspolczynniki)
    sum = 0
    for i, wsp in enumerate(wspolczynniki):
        sum += wsp * x ** (dl - 1)
        dl = dl - 1
    sum = round(sum, 2)
    if "precyzja" in opcjonalne and isinstance(opcjonalne["precyzja"], int):
        round(sum, opcjonalne["precyzja"])
    if "dziedzina" in opcjonalne and isinstance(opcjonalne["dziedzina"], dict):
        x1 = opcjonalne["dziedzina"].get(0)
        x2 = opcjonalne["dziedzina"].get(1)
        if x > x1 and x < x2:
            return sum
        else:
            return "x wykracza poza dziedzine"

    return sum


result = polynomial_calculator(2, 2, 3, 1, 1)
print(result)
