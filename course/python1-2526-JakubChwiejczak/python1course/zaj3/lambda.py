ksiazki = [
    {"tytul": "Władca Pierścieni", "autor": "J.R.R. Tolkien", "rok_wydania": 1954},
    {
        "tytul": "Harry Potter i Kamień Filozoficzny",
        "autor": "J.K. Rowling",
        "rok_wydania": 1997,
    },
    {"tytul": "Duma i uprzedzenie", "autor": "Jane Austen", "rok_wydania": 1813},
    {"tytul": "Rok 1984", "autor": "George Orwell", "rok_wydania": 1949},
    {"tytul": "Zbrodnia i kara", "autor": "Fiodor Dostojewski", "rok_wydania": 1866},
    {"tytul": "Mistrz i Małgorzata", "autor": "Michaił Bułhakow", "rok_wydania": 1967},
    {"tytul": "Hobbit", "autor": "J.R.R. Tolkien", "rok_wydania": 1937},
    {
        "tytul": "Sto lat samotności",
        "autor": "Gabriel García Márquez",
        "rok_wydania": 1967,
    },
    {"tytul": "Imię róży", "autor": "Umberto Eco", "rok_wydania": 1980},
    {"tytul": "Solaris", "autor": "Stanisław Lem", "rok_wydania": 1961},
]

ksiazki_sorted = sorted(ksiazki, key=lambda x: x["rok_wydania"])
print(ksiazki_sorted)
ksiazki_filtered = list(filter(lambda x: x["rok_wydania"] > 2000, ksiazki))
print(ksiazki_filtered)
ksiazki_tytul = list(map(lambda x: x["tytul"], ksiazki))
print(ksiazki_tytul)
# -------------------------------
pary = lambda x, y: x % 2 == 0 and y % 2 == 0
print(pary(2, 4))
print(pary(3, 6))

# --------------------------------
nazw = ["Anna Kowalska", "Jan Nowak", "Piotr Wiśniewski", "Ewa Zielińska"]
nazw_s = sorted(nazw, key=lambda x: x.split()[1])
print(nazw_s)
nazw_i = list(map(lambda x: x.split()[0][0] + x.split()[1][0], nazw))
print(nazw_i)
