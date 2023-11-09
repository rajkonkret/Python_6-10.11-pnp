# Zapytania REST API korzystają ze standardowych metod HTTP:
# GET, POST, PUT / PATCH, DELETE.
# Operacje te to CREATE, READ, UPDATE, DELETE, w skrócie CRUD.
# w bazie danych: INSERT, SELECT, UPDATE, DELETE
import requests as re

# zaimportowanie biblioteki jako alias(re) - mamy mniej pisania podczas uzywania tej biblioteki w kodzie
# pip install requests
url = 'http://api.nbp.pl/api/exchangerates/rates/A/CHF/'

response = re.get(url)
print(response)  # <Response [200]>
# 200  -ok
# 400 - np.: bad request - bład np.: parametr błedny
# 3xx - przekierowania
# 4xx - bład po stronie klienta
# 5xx = bład po stronie serwera
table = response.json()
print(table)
# {'table': 'A', 'currency': 'frank szwajcarski', 'code': 'CHF',
#  'rates': [{'no': '216/A/NBP/2023', 'effectiveDate': '2023-11-08', 'mid': 4.6343}]}
# wypisac wszystkie klucze
# wypisac wartosci dla wszystki klucze
print(type(table))  # <class 'dict'>
print(table.keys())  # dict_keys(['table', 'currency', 'code', 'rates'])
print(table['table'])
print(table['currency'])
print(table['code'])
print(table['rates'])  # [{'no': '216/A/NBP/2023', 'effectiveDate': '2023-11-08', 'mid': 4.6343}]
print(table['rates'][0])  # {'no': '216/A/NBP/2023', 'effectiveDate': '2023-11-08', 'mid': 4.6343}
print(table['rates'][0].keys())  # dict_keys(['no', 'effectiveDate', 'mid'])
for k, v in table['rates'][0].items():
    print(k, "=>", v)
# no => 216/A/NBP/2023
# effectiveDate => 2023-11-08
# mid => 4.6343
rates = table['rates'][0]
print(table['rates'][0]['no'])
print(table['rates'][0]['effectiveDate'])
print(table['rates'][0]['mid'])
# 216/A/NBP/2023
# 2023-11-08
# 4.6343
print(rates['no'], rates['effectiveDate'], rates['mid'])  # 216/A/NBP/2023 2023-11-08 4.6343
# pobrac ceny złota?
url = 'http://api.nbp.pl/api/cenyzlota'
# pydantic
response_gold = re.get(url)
table_gold = response_gold.json()
print(table_gold)  # [{'data': '2023-11-09', 'cena': 263.32}]
print(table_gold[0]['data'])
print(table_gold[0]['cena'])
# 2023-11-09
# 263.32
