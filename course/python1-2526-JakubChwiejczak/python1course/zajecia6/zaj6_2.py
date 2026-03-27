def days(max_val):
    day = [
        "poniedzialek",
        "wtorek",
        "sroda",
        "czwartek",
        "piatek",
        "sobota",
        "niedziela",
    ]
    i = 0
    while i < 7:
        yield day[i]
        i = i + 1


D = days(3)
print(next(D))
print(next(D))

for day in days(7):
    print(day)
