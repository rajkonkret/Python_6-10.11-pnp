# klasy - szablon (przepis, opis)  wg którego bedziemy budować obiekty
# kalsa moze posiadac pola (zmienne), funkcje (metody)
# obiekt - element zbudowany na podstawie klasy
# obiekt jest instancja klasy


class Human:  # definicja klasy
    """
    Klasa opisująca człowieka w Pythonie
    """
    imie = ""
    wiek = None
    plec = "k"

    def powitanie(self):
        """
        dokumentacja. Klasa wypisuje imie obiektu z klasy Human
        :return: None
        """
        print(f"Nazwyam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Masz {self.wiek} lat")


# uzycie klasy
cz1 = Human()  # tworzenie obiektu kalsy Human
print(Human.__doc__)  # Klasa opisująca człowieka w Pythonie
print(print.__doc__)
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
cz1.imie = "Ania"
cz1.wiek = 28
print(cz1)  # <__main__.Human object at 0x0000023C613614D0>
print(cz1.plec)
print(cz1.wiek)
print(cz1.imie)
# stworzec obiekt klasy Human, płci innej
cz2 = Human()  # tworzenie obiektu kalsy Human
print(Human.__doc__)  # Klasa opisująca człowieka w Pythonie
print(print.__doc__)
print(cz2.plec)
print(cz2.wiek)
print(cz2.imie)
cz2.imie = "Tomek"
cz2.wiek = 28
cz2.plec = "m"
print(cz2)  # <__main__.Human object at 0x0000023C613614D0>
print(cz2.plec)
print(cz2.wiek)
print(cz2.imie)

cz1.powitanie()
cz2.powitanie()
# Nazwyam się Ania
# Nazwyam się Tomek
# dopisac funkcję (metode) wypisz_wiek()
cz1.wypisz_wiek()
cz2.wypisz_wiek()
