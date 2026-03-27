import matematyka

wynik = matematyka.dodaj(5, 3)
print(f"wynik dodawania:{wynik}")

wynik2 = matematyka.odejmij(8, 2)
print(f"wynik odejmowania:{wynik2}")


x = 10  # Zmienna globalna


def funkcja():
    x = 5  # Zmienna lokalna
    print(f"Wartość x wewnątrz funkcji: {x}")


funkcja()
print(f"Wartość x na poziomie globalnym: {x}")
