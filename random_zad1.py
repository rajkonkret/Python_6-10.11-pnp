import random

# random - biblioteka do działania (generownia) liczb pseudolosowych

print(random.randint(1, 6))  # int 1 .. 6
print(random.random())  # float 0.6881351466124862  0....0.999999
print(random.random() * 6)  # float 5.4677669233236482  0....5.999999
print(random.randrange(6))  # int 0 .. 5
print(random.randrange(1, 6))  # int 1..5

lista = [5, 7, 45, 34, 56]
print(random.choice(lista))  # 56

lista2 = list(range(1, 50))  # 1..49
print(lista2)
# [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14,
# 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27,
# 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40,
# 41, 42, 43, 44, 45, 46, 47, 48, 49]

wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)
wyn = random.choice(lista2)
lista2.remove(wyn)
print(wyn)

print(random.choices(lista2, k=6))  # losuje z powtórzeniami [11, 10, 20, 32, 10, 20]
print(random.sample(lista2, 6))  # [29, 23, 42, 43, 45, 17] - losuje bez powtórzen
print(random.sample(lista2, k=6))  # [14, 11, 31, 2, 33, 13] - losuje bez powtórzen
