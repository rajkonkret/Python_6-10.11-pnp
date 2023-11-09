# pliki csv - dane sa rozdzielone znakiem podziału (,)
# , ; tab i inne
# Zenek, Marek, Tomek
import csv

# biblioteka do pracy z danymi typu csv
fields = ['name', 'branch', 'year', 'cgpa']
row = ['radek', 'coe', '3', '0']

zipped_dict = dict(zip(fields, row))
print(zipped_dict)
dict_list = [
    {'name': 'radek', 'branch': 'coe', 'year': '3', 'cgpa': '9'},
    {'name': 'Zosia', 'branch': 'cos', 'year': '2', 'cgpa': '9.1'},
    {'name': 'Tomek', 'branch': 'cot', 'year': '1', 'cgpa': '0.5'},
    {'name': 'Zenek', 'branch': 'con', 'year': '8', 'cgpa': '00'},
]

filename = 'records.csv'

with open(filename, 'w', newline='', encoding='utf-8') as csv_f:
    # dla działania z listą
    # csvwriter = csv.writer(csv_f)
    # csvwriter.writerow(fields)
    # csvwriter.writerow(row)
    # Dla działan ze słownikiem
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields)
    csvwriter.writeheader()
    # csvwriter.writerow(zipped_dict)  # zapisanie jedego wiersza ze słownika
    csvwriter.writerows(dict_list)  # zapisanie  z listy słowników
