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
