# klucz - wartosc
# {'klucz' : 'wartosc' }
# klucz nie może się powtarzać
# slownik - typ danych o budowie para klucz - wartość

dictionary = {}  # tworzenie pustego słownika
print(dictionary)  # {}
print(type(dictionary))  # <class 'dict'>

dictionary['imie'] = 'Radek'
print(dictionary)
# dodac klucz wiek, i jakas wartosc dla niego
dictionary['wiek'] = 35
print(dictionary)  # {'imie': 'Radek', 'wiek': 35}

print(dictionary.keys())
print(dictionary.values())
print(dictionary.items())
# dict_keys(['imie', 'wiek'])
# dict_values(['Radek', 35])
# dict_items([('imie', 'Radek'), ('wiek', 35)])

dictionary.update({'date': '12-12-2023'})
print(dictionary)  # {'imie': 'Radek', 'wiek': 35, 'date': '12-12-2023'}

dict2 = {'x': 2}
dict2.update([("y", 5), ("z", 7)])
print(dict2)  # {'x': 2, 'y': 5, 'z': 7}

# utworzyc słownik, gdzie beda pary polskiełsowo-angileskie tłumaczenie
dict_p_e = {"imie": 'name', 'kot': 'cat'}
print(dict_p_e['imie'])  # name

# pokazemy jakie słowka umiemy tłumaczyc
# zapytamy uzytkownika jakie słowko chce przetłumaczyc
# wypiszemy mu tłumaczenie
# print(f"Umiem przetłumaczyc: {dict_p_e.keys()}")
# key = input("Podaj słowo do przetłumaczenia")
# print(dict_p_e[key.replace(" ", "").lower()])

# kalkulator
# pobrac a i b od uzytkownika
# wyswietlic wynik działania np.: dodawania
a = input("Podaj pierwszą liczbę")  # input zwraca stringa
b = float(input("Podaj drugą liczbę"))
print(type(a))  # <class 'str'>
print(int(a) + b)  # 9.0
# hackerrank
# eval()
print(eval("5 + 5"))
a = "6"
b = "7"
wyr = a + "+" + b
print(eval(wyr))
