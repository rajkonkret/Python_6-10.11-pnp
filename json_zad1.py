# json  - para klucz - wartosc
# '{"name":"John", "age":30, "car":null}'
# obiekt uzywany głownie do komunikacji miedzy systemami
# czasami npp w pliku konfiguracyjnym
import json

person_dict = {'name': 'Radek', 'age': 40, 'czy_pali': None}
print(type(person_dict))  # <class 'dict'>

with open('nasze_dane.json', 'w') as f:
    json.dump(person_dict, f, indent=4, sort_keys=True)
# {
#     "name": "Radek",
#     "age": 40,
#     "czy_pali": null
# }
# sort_keys=True - sortowanie po nazwie klucza
# indent=4 - wciecie 4 spacje

with open('nasze_dane.json', 'r') as fh:
    data = json.load(fh)

print(data)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
print(type(data))  # <class 'dict'>
print(data['name'])  # Radek

# zamiana słownika na jsona
json_text = json.dumps(data)
print(json_text)  # {"age": 40, "czy_pali": null, "name": "Radek"}

# zammiana jsona na słownik
string_json = json.loads(json_text)
print(string_json)  # {'age': 40, 'czy_pali': None, 'name': 'Radek'}
