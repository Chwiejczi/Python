import math

lista1 = [x**2 for x in range(1, 20) if (x**2) % 3 == 0]
print(lista1)

# ----------------------------
imiona = ["Anna", "Jan", "Ewa", "Piotr"]
oceny = [5, 4, 3, 5]
lista2 = [{x: y} for x, y in zip(imiona, oceny)]
print(lista2)
# -------------------------------------
lista3 = [str(x) for x in range(1, 50) if x % 3 == 0 and x % 5 == 0]
print(lista3)
# ------------------------------------------------------
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
lista4 = [x**2 for podlista in l for x in podlista]
print(lista4)
# -----------------------------------------
lista5 = [x**2 for x in range(1, 100) if math.sqrt(x) == int(math.sqrt(x))]
print(lista5)
