# for - petla iteracyjna
import random
from itertools import zip_longest

for i in range(10):  # 0..9
    print(i, end=' ')
# end= -  znak konca lini (domyslnie \n(enter))
print()
for i in range(10):
    pass  # nic nie robi

for _ in range(10):  # niema zmienna
    # print(_)
    pass

for i in range(10):
    print(i * 2, end=" ")  # 0 2 4 6 8 10 12 14 16 18
print()
# losowanie liczb z wykorzystaniem remove() na liscie z uzyciem pętli for
# zaimportowac randoma
# wygenerowac liczby od 1 .. 49
# w petli pobierac szesc liczb (losowac) z listy, wyswietlac i usuwac
lista = list(range(1, 50))
lista_wyniki = []
for i in range(6):
    wyn = random.choice(lista)
    lista.remove(wyn)
    lista_wyniki.append(wyn)

print(lista_wyniki)
# posortowac
lista_wyniki.sort()
print(lista_wyniki)  # [3, 22, 24, 28, 43, 49]
lista_wyniki.sort(reverse=True)  # sortuje i odwraca
lista_wyniki.reverse()  # tylko odwraca

for i in range(10):
    if i % 2 == 0:  # % - modulo - reszta z dzielenia
        print(i, "jest parzysta")

lista3 = [j for j in range(1, 10) if j % 2 == 0]
print(lista3)  # [2, 4, 6, 8]
print(type(lista3))  # <class 'list'>

for c in lista3:
    if c == 2:
        c += 1  # c = c + 1
    print(c)

a = 1
a += 1  # a = a + 1
print(a)  # 2
a -= 1  # a = a - 1
print(a)  # 1
a *= 2  # a = a * 2
print(a)  # 2
a /= 2  # a = a / 2
print(a)  # 1.0 - float zawsze
a %= 2  # a = a % 2  % - reszta z dzielenia
print(a)

imiona = ['Radek', "Zenek", "Tomek"]

for p in imiona:
    print(p)
# Radek
# Zenek
# Tomek

# wyswietlic elementy z takiej listy imion z numerem indeksu
# 0 Radek
for p in imiona:
    print(imiona.index(p), p)  # 0 Radek

for i in range(len(imiona)):  # range(3) 0 .. 2
    print(i, imiona[i])  # 0 Radek

# enumerate() - numeruje kolekcje, zwraca nadany indeks i element
for p in enumerate(imiona):
    print(p)  # (0, 'Radek') krotka

a, b = (0, 'Radek')
print(a, b)  # 0 Radek
for p, o in enumerate(imiona, start=1):  # rozpakowanie krotki podczas pobierania danych w petli p, o = (0, 'Radek')
    if p >= 1:
        print(p, o)  # 1 Radek start = poczatek numeracji

# for p, o in enumerate(imiona):  # rozpakowanie krotki podczas pobierania danych w petli p, o = (0, 'Radek')
#     print(p, o)  # 0 Radek
# 14:00 - dajcie jescze 5 minut
for i in range(1, len(imiona)):
    print(i, imiona[i])
# 1 Zenek
# 2 Tomek

ludzie = ['Radek', 'Janek', 'Asia', 'Romek', "Artur"]
# ludzie = ['Radek', 'Janek', 'Asia', 'Romek']
wiek = [47, 57, 32, 34]

# wypisaniu imienia i odpowidającego mu wieku
# # gdy długości list różne: IndexError: list index out of range
# for x in range(len(ludzie)):
#     print(ludzie[x], wiek[x])
#
# for i in ludzie:
#     print(i, wiek[ludzie.index(i)])

# zip() - łaczy dwie listy w jedna
for i in zip(ludzie, wiek):
    print(i)  # ('Asia', 32)

for o, w in zip(ludzie, wiek):
    print(o, w, sep=";")
# Radek;47
# Janek;57
# Asia;32
# Romek;34
# sep= - znak separacji pomiedzy przecinkami(domyslnie spacja)

# 0 Radek 47
for i in enumerate(zip(ludzie, wiek)):
    print(i)  # (3, ('Romek', 34))

a, b = (3, ('Romek', 34))
print(a)
print(b)  # ('Romek', 34)
imie, wiek2 = ('Romek', 34)
indeks, (imie, wiek2) = (3, ('Romek', 34))
print(indeks, imie, wiek2)  # 3 Romek 34

for indeks, (imie, wiek2) in enumerate(zip(ludzie, wiek)):
    print(indeks, imie, wiek2)
# 0 Radek 47
# 1 Janek 57
# 2 Asia 32
# 3 Romek 34

zipped = zip_longest(ludzie, wiek, fillvalue='Nan')
print(type(zipped))  # <class 'itertools.zip_longest'>
zipped_list = list(zipped)
for name, age in zipped_list:
    print(name, age)
# Radek 47
# Janek 57
# Asia 32
# Romek 34
# Artur Nan
# dodac indeksy
for p in enumerate(zipped_list):
    print(p)
for i, (o, w) in enumerate(zipped_list):
    print(i, o, w)  # 4 Artur Nan

c = {'name': 'Radek', 'age': '5'}
# {'Radek': 'name', '5': 'age'}
# słownik
print({v: k for k, v in c.items()})  # {'Radek': 'name', '5': 'age'}
