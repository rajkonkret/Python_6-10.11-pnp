def odejmij(a, b):
    return a - b


# funkcja zwraca wynik odejemowania


print(odejmij(7, 8))

# funkcja labda - skrocony zapis funkcji
odejmij2 = lambda a, b: a - b  # labda ma return domyslnie
print(odejmij2(9, 8))


# przerobic oblicz_vat na lambde
def oblicz_vat(cena, vat=23):
    return cena * (100 + vat) / 100


oblicz_vat2 = lambda cena, vat=23: cena * (100 + vat) / 100
print(oblicz_vat2(1000))  # 1230.0

wiek = lambda x: "dziecko" if x < 10 else ("nastolatek" if x < 18 else "dorosły")
print(wiek(8))
print(wiek(10))
print(wiek(18))
# dziecko
# nastolatek
# dorosły

lista = [1, 2, 3, 4, 5, 6, 20, 25, 50, 80]
l = []
for i in lista:
    l.append(i * 2)


def zmien(x):
    return x * 2


print(l)  # [2, 4, 6, 8, 10, 12, 40, 50, 100, 160]
# map() - bieze kazdy element, zmienic elemnty wg zadanej funkcji
print(f"Zastosowanie map(): {list(map(zmien, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 10, 12, 40, 50, 100, 160]
print(f"Zastosowanie map(): {list(map(lambda x: x * 2, lista))}")
# Zastosowanie map(): [2, 4, 6, 8, 10, 12, 40, 50, 100, 160]

# filter() - filtrowanie danych wg zadanej funkcji
print(f"Zastosowanie filter(): {list(filter(lambda x: x < 3, lista))}")
# Zastosowanie filter(): [1, 2]
# x > 8 - wyfiltrowac
print(f"Zastosowanie filter(): {list(filter(lambda x: x > 8, lista))}")
# Zastosowanie filter(): [20, 25, 50, 80]
# x > 3 i x < 20 - wyfiltrowac
print(f"Zastosowanie filter(): {list(filter(lambda x: 3 < x < 20, lista))}")
#  x > 3 and x < 20 -> 3 < x < 20
# Zastosowanie filter(): [4, 5, 6]
