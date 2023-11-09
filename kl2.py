class Human:
    """
    Klasa opisująca człowieka w pythonie
    """

    # self oznacza obiekt który wywołuje metody lub pola
    def __init__(self, imie, wiek, plec="k"):  # inicjalizator (konstruktor)
        self.imie = imie
        self.wiek = wiek
        self.plec = plec

    def powitanie(self):
        """
        dokumentacja. Klasa wypisuje imie obiektu z klasy Human
        :return: None
        """
        print(f"Nazwyam się {self.imie}")

    def wypisz_wiek(self):
        print(f"Masz {self.wiek} lat")

    def wypisz_plec(self):
        print(f'Jestem {self.plec}')

    def ruszaj(self):
        if self.plec == "k":
            print("Ruszyłam w drogę")
        else:
            print("Ruszyłem w drogę")


cz1 = Human("Ania", 29)
print(cz1.imie)
print(cz1.plec)
print(cz1.wiek)
# Ania
# k
# 29

# dopisac metody powitanie, wypisz_wiek, wypisz_plec
cz1.wypisz_plec()

cz2 = Human("Radek", 45, "m")
cz2.wypisz_plec()
cz1.ruszaj()
cz2.ruszaj()
# k
# 29
# Jestem k
# Jestem m
# Ruszyałam w drogę
# Ruszyłem w drogę
