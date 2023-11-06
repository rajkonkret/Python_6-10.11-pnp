teksty = "Witaj świecie"
print(teksty)  # Witaj świecie
print(teksty.upper())  # WITAJ ŚWIECIE
print(teksty)  # Witaj świecie
# tekst jest niemutowalny
# """ Return a copy of the string converted to uppercase. """
# nie zostaje zmieniony oryginalny tekst, tylko dostajemy kopie ze zmiana
tekst2 = teksty.upper()
print(tekst2)  # WITAJ ŚWIECIE

# zamian ana małe litery, uzyc: lower()
tekst3 = teksty.lower()
print(tekst3)

print(teksty.removeprefix("Witaj"))  # " świecie"
print(teksty.removesuffix("świecie"))  # "Witaj "
print(teksty)  # Witaj świecie

print(teksty.count("i"))  # 3
print(teksty.count("i", 0, 4))  # 1
# Witaj
# 01234 - kolejne pozycje znaków
print(teksty.count("j", 0, 4))  # 0 0,4 oznacza ze bierze indeksy od 0 do 3

# kodowanie znaków
encoded_s = teksty.encode('utf-8')
print(encoded_s)  # b'Witaj \xc5\x9bwiecie'
# b - zapis binarny
print(type(encoded_s))  # <class 'bytes'>
print(encoded_s.decode('utf-8'))
# Witaj świecie

imie = "Radek"
print(imie)
# f- string - sformatowane stringi
tekst_format = f"\tMam na imię {imie}\n i lubię Pythona\b"
print(tekst_format)  # Mam na imię Radek
#    Mam na imię Radek
# i lubię Python
# \t - tabulaor
# \n - nowa linia
# \b - backspace

starszy = 'wiataj %s!'
print(starszy % imie)  # wiataj Radek!
print("Witaj {}!".format(imie))
print("""
    Tekst
Wielolinijkowy
""")
#     Tekst
# Wielolinijkowy
