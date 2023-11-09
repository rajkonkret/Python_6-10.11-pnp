import csv

filename = 'records.csv'

fileds = []
rows = []

with open(filename, 'r') as csv_f:
    dialect = csv.Sniffer().sniff(csv_f.read(1024))
    print(dialect.delimiter, dialect.quotechar)  # ; "
    # csvreader = csv.reader(csv_f, delimiter=';')
    csvreader = csv.reader(csv_f, delimiter=dialect.delimiter)
    print(csvreader)  # <_csv.reader object at 0x00000192580C7160>, iterator, ma wewnetrzny licznik,
    # za kazdym odczytaniem przestawiany jest o jeden do przodu
    csv_f.seek(0)  # zerowanie licznika odczytu dla tego pliku
    fields = next(csvreader)  # odczytanie zerowego elemntu i ustawienie wskaznika na nastepny

    for row in csvreader:  # petla juz pobiera od elementu o indeksie 1 (czyli drugiego elementu)
        rows.append(row)

print(rows)  # [['radek', 'coe', '3', '9'], ['Zosia', 'cos', '2', '9.1'],
# ['Tomek', 'cot', '1', '0.5'], ['Zenek', 'con', '8', '00']]
print(fields)  # ['name', 'branch', 'year', 'cgpa']
# 11:25
