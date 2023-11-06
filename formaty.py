user = "Tomek"  # str
wiek = 39  # int
wersja = 3.900001  # float - liczba zmiennoprzecinkowa
liczba = 134567112456  # int

print("Witaj %s masz teraz %d lat" % (user, wiek))
# print("Witaj %d masz teraz %s lat" % (user, wiek))  # TypeError: %d format: a real number is required, not str
# %s - string
# %d - digit całkowita)
print("Witaj %(user)s, masz teraz %(age)d lat." % {'user': user, 'age': wiek})  # Witaj Tomek, masz teraz 39 lat.

print(f"Witaj {user}, maasz teraz {wiek} lat.")  # f - f-string
print(f"Witaj {wiek}, maasz teraz {user} lat.")  # f - f-string
# Witaj 39, maasz teraz Tomek lat.
# 13:20

print("Używamy wersji pythona %i" % 3)
print("Używamy wersji pythona %f" % 3.8)  # Używamy wersji pythona 3.800000
print("Używamy wersji pythona %.1f" % 3.8)  # Używamy wersji pythona 3.8
print("Używamy wersji pythona %.2f" % 3.8)  # Używamy wersji pythona 3.80
print("Używamy wersji pythona %.0f" % 3.8)  # Używamy wersji pythona 4
print("Używamy wersji pythona %.f" % 3.8)  # Używamy wersji pythona 4
# wykonyje zaokrąglenie przy wypisywaniu
print("Używamy wersji Python {}".format(wersja))  # Używamy wersji Python 3.900001
print(f"Używamy wersji Python {wersja}")  # Używamy wersji Python 3.900001

print(f"Używamy wersji Python {wersja}")
print(f"Używamy wersji Python {wersja:.1f}")  # Używamy wersji Python 3.9
print(f"Używamy wersji Python {wersja:.2f}")  # Używamy wersji Python 3.90
print(f"Używamy wersji Python {wersja:.0f}")  # Używamy wersji Python 4

print(f"{user:>10}")  # "     Tomek"
print(f"{user:>20}")  # "               Tomek"
print(f"{user:<20}")  # "Tomek               "
print(f"{user:^10}")  # "  Tomek   "

print(liczba)  # 134567112456
print("Nasza duża liczba {:,}".format(liczba))  # Nasza duża liczba 134,567,112,456
print("Nasza duża liczba {:,}".format(liczba).replace(",", "."))  # Nasza duża liczba 134.567.112.456
print("Nasza duża liczba {:,}".format(liczba).replace(",", " "))  # Nasza duża liczba 134 567 112 456
print(f"Liczba {liczba:,}".replace(",", " "))  # Liczba 134 567 112 456


