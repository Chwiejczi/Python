# L = [1,2,3,4]
# M = [1,2,3,L,4]
# print(f"Wartość zmiennej M przed zmianą L: {M}")
# L[1] = "woooow"
# print(f"Wartość zmiennej M po zmianie L: {M}")


L = [4, 5, 6]
X = L * 4
Y = [L] * 4
print(f"X: {X}, Y: {Y}")
L[1] = "wow"
print(f"X: {X}, Y: {Y}")
