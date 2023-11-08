# funkcja zwracająca wynik
def dodaj(a, b):
    return a + b  # return zwraca wynik


def odejmij(a=0, b=0, c=0):  # try argumenty domyslne
    return a - b - c


def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


print(dodaj(5, 6))

# napisac funkcję, ktora posiada trzy argumenty,
# zwraca wynik (np odejmowanie)
# jeden argument wartosc domyslna
# uzyc ja na kilka mozliwych sposobow
print(odejmij(1, c=7, b=9))
print(odejmij(3, 4, 5))
print(odejmij(3))
print(odejmij())
print(oblicz_vat(1000))
print(oblicz_vat(1000, 7))
print(oblicz_vat(vat=8, cena=1000))
# jak juz podamy argumenty po nazwie, to nie mozna juz podawac argumentu pozycyjnego
# print(odejmij(b=8, c=9, 2))  # SyntaxError: positional argument follows keyword argument
# 11
# -15
# -6
# 3
# 0
# 1230.0
# 1070.0
# 1080.0
