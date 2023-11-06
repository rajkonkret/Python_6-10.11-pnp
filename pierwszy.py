print()  # wypisz/drukuj
# ctrl alt l
# pep8
print("Nazywam się Radek")
print("Dowolny tekst")  # ctrl d - powielanie danej lini
print('Dowolny tekst')  # można stosować pojedyncze cudzysłowy
# 'Dowolny tekst' - to jest typ str (string) - teksty
print(39)

print(type("Radek"))  # <class 'str'>
print(type(39))  # <class 'int'> - liczby całkowite
# type() - sprawdzenie typu danej
print("39" + "14")  # 3914
print(5 * "4")  # 44444
print(39 + 14)
print(int("39") + int("14"))  # 53
# int() - rzutowanie na int
# zmienna

imie = "Radek"
print(imie)
print(type(imie))  # <class 'str'>

wiek = 48
print(wiek)
print(type(wiek))  # <class 'int'>

imie = 47
print(type(imie))  # <class 'int'>

imie = "Ola"
# print(imie + wiek)  # TypeError: can only concatenate str (not "int") to str
print(imie + str(wiek))  # Ola48
# ctrl / - komentowanie lini z kursorem
# str() - rzutowanie na string
