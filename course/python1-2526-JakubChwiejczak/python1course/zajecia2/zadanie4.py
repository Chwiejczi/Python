imiona = ["Jan", "Adam", "Marek", "Arek", "Jarek"]
for i, name in enumerate(imiona):
    print(f"imie: {name}, o indeksie: {i}")


num = 2

if num > 0 and num % 2 == 0:
    print("liczba jest dodatnia i parzysta")

if num != 0:
    print("liczba jest rozna od 0")


fruits = ["jabłko", "banan", "pomarańcza"]

fruit = "banan"
if fruit in fruits:
    print("owoc jest dostępny")
else:
    print("nie ma takiewgo owoca")


sum = 0

while sum < 100:
    number = float(input())
    sum = sum + number
print(f"sum={sum}")
