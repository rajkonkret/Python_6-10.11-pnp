# set (zbiór) - przechowuje niezduplikowane elementy
# nie zachowuje kolejnosci przy dodawaniu elementów

lista = [44, 55, 66, 777, 33, 22, 11, 33, 11]
zbior = set(lista)  # zamiana na set
print(zbior)  # {33, 66, 777, 11, 44, 22, 55}

zb2 = set()  # tworzenie pustego seta
print(zb2)  # set()
print(type(zb2))  # <class 'set'>

zb2.add(2)
zb2.add(3)
zb2.add(5)
zb2.add(5)
print(zb2)  # {2, 3, 5}

zbior.add(33)
zbior.add(18)
zbior.add(18)
print(zbior)  # {33, 66, 777, 11, 44, 18, 22, 55}
print(zbior.pop())  # 33
print(zbior)  # {66, 777, 11, 44, 18, 22, 55}
zbior.pop()
zbior.pop()
zbior.pop()
print(zbior)  # {44, 18, 22, 55}

zbior.remove(55)
zbior.remove(18)
print(zbior)  # {44, 22}

zbior2 = {667, 11, 44, 18, 52, 62, 999, 999}
print(zbior2)  # {18, 52, 999, 11, 44, 667, 62}

print(zbior | zbior2)  # {999, 11, 44, 18, 52, 22, 667, 62} - suma zbiorów
print(zbior & zbior2)  # {44} - częśc wspolna
print(zbior - zbior2)  # {22} różnica
print(zbior.difference(zbior2))  # {22}

zbior3 = {1, 2, 3, 3, 44, 55, 44}
zbior3.add(5)
zbior3.add(5)
zbior3.add(8)
print(zbior3)  # {1, 2, 3, 5, 55, 8, 44}
zbior3.clear()
print(zbior3)  # set() - pusty zbiór
