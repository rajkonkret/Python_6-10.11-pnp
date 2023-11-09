import csv

lista = []

with open('dane.csv', 'r') as file:
    reader = csv.reader(file)
    for i in reader:
        lista.append(i)

print(lista)  # [['SN', ' Name', ' City'], ['1', ' Michael', ' New Jersey'], ['2', ' Jack', ' California']]
# odczytac Micheala
print(lista[1])  # ['1', ' Michael', ' New Jersey']
print(lista[1][1])  # Michael

lista[1][1] = "Radek"

with open('dane2.csv', 'w', newline="", encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerows(lista)
