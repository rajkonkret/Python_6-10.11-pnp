# lista - kolekcja, przechowywac na raz różne typy
# zachowuje kolejność dodawania
lista = []  # pusta lista
print(lista)
print(type(lista))  # <class 'list'>

lista.append("Radek")
lista.append("Maciek")
lista.append("Jaśko")
lista.append("Grzesiek")
print(lista)  # ['Radek', 'Maciek', 'Jaśko', 'Grzesiek']
#                 0(-4)     1(-3)     2(-2)     3(-1)
# indeksowanie od 0
print(lista[0])  # Radek
# wypisac dwa dowolne elementy z listy po indeksie
print(lista[2])
print(lista[3])
# print(lista[10])  # IndexError: list index out of range

print(lista[3])
print(len(lista))
print(lista[-1])  # ostatni element z listy
print(lista[-3])  # Maciek
print(lista[0:3])  # ['Radek', 'Maciek', 'Jaśko'] od indeksu 0 do indeksu 2
print(lista[:3])  # ['Radek', 'Maciek', 'Jaśko']
print(lista[0:-2])  # ['Radek', 'Maciek']
print(lista[-2:0])  # [] bo nie jest w stanie isc w strone zera, idzie w prawo a zero po lewej

# nadpisanie elemntu na danym indeksie
lista[2] = "Mikołaj"
print(lista)  # ['Radek', 'Maciek', 'Mikołaj', 'Grzesiek']
# elemnt został zastąpiony

# dodanie elementu do listy we wskazanym miejscu
lista.insert(1, "Marcin")
print(lista)  # ['Radek', 'Marcin', 'Maciek', 'Mikołaj', 'Grzesiek']

# usuniecie elementu (pierwszy napotkany)
lista.remove("Maciek")
print(lista)  # ['Radek', 'Marcin', 'Mikołaj', 'Grzesiek']

# sprawdzenie indeksu dla elemntu
indeks = lista.index("Grzesiek")
print(indeks)  # 3

# usunięcie elementu po indeksie
print(lista.pop(indeks))  # Grzesiek - pop() zwraca element, który usunęlismy
print(lista)  # ['Radek', 'Marcin', 'Mikołaj']
# 15:05
print(lista.pop())  # Mikołaj

a = 1
b = 3
a = b
print(a)  # 3
b = 7
print(a)  # 3

lista2 = lista
lista3 = lista.copy()  # kopiowanie zawartosci listy jedej do drugiej
print(lista)  # kopiowanie referencje (adres w pamięci)
print(lista2)
lista.clear()  # wyczysc wszystko z listy
print(lista2)  # []
print(lista)
print(id(lista))  # 2331951321344
print(id(lista2))  # 2331951321344
print(lista3)  # ['Radek', 'Marcin']
print(id(lista3))  # 2249673570368

liczby = [54, 999, 34, 22, 12.34, 687]
# liczby = [54, 999, 34, 22, 12.34, 687, "A"]  # TypeError: '<' not supported between instances of 'str' and 'int'
print(liczby)  # [54, 999, 34, 22, 12.34, 687]
liczby.sort()
print(liczby)  # [12.34, 22, 34, 54, 687, 999]

lista_osoby = ['radek', 'ola', 'zenek']
lista_osoby.sort()  # sortowanie kolekcji
print(lista_osoby)  # ['ola', 'radek', 'zenek']
lista_osoby.reverse()  # odwracanie kolekcji
print(lista_osoby)  # ['zenek', 'radek', 'ola']
lista_osoby.sort(reverse=True)  # ['zenek', 'radek', 'ola'] - sortowanie i odwrócenie kolekcji

liczby[3] = 6666
print(liczby)

# usunac element o indeksie 3, usunac element (liczbę) 34 z tej listy
liczby.pop(3)
liczby.remove(34)
print(liczby)  # [12.34, 22, 687, 999]
print(len(liczby))  # 4

tekst = 'Python'
lista_1 = list(tekst)  # list() - rzutownai na listę
print(lista_1)  # ['P', 'y', 't', 'h', 'o', 'n']  # rozpakowanie sekwencji

lista_2 = [tekst]
print(lista_2)  # ['Python']

krotka = tuple(liczby)  # zamiana listy na krotke (tuple)
print(type(krotka))  # <class 'tuple'>
print(krotka)  # (12.34, 22, 687, 999)
