import chardet

# pip install chardet

file_path = 'test.log'

with open(file_path, 'rb') as file:
    raw_data = file.read()

result = chardet.detect(raw_data)  # próba odszyfrowania kodowania pliku
print(result)
# dla małej próbki możemy mieć błedny odczyt
# {'encoding': 'Windows-1254', 'confidence': 0.670697820753897, 'language': 'Turkish'}
# po dodaniu większej ilości polskich znaków w pliku mamy juz dokładniejszą informację
# 'confidence': 0.87625
# {'encoding': 'utf-8', 'confidence': 0.87625, 'language': ''}
encoding = result['encoding']
print(raw_data.decode(encoding=encoding))
# Radek
# Dodane
# Dodane
# Dodane
# Dośąńdane
