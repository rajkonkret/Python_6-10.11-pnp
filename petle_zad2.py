dictionary = {'imie': "Radek", 'nazwisko': "Kowalski"}
print(dictionary)
print(type(dictionary))

# wypisze klucze
for k in dictionary:
    print(k)

for k in dictionary.keys():
    print(k)

# wypisze wartości
for v in dictionary.values():
    print(v)

for i in dictionary.items():
    print(i)  # ('imie', 'Radek')

for k, v in dictionary.items():
    print(k, "=>", v)  # nazwisko => Kowalski

c = {'name': 'Radek', 'age': '5'}
# {'Radek': 'name', '5': 'age'}
# słownik
print({v: k for k, v in c.items()})  # {'Radek': 'name', '5': 'age'}

d2 = {}
for key, value in c.items():
    d2.update({value: key})
print(d2)
{'Radek': 'name', '5': 'age'}
{'Radek': 'name', '5': 'age'}
