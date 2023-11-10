class Dom:
    """
    Klasa opisująca dom w pythonie
    """

    def __init__(self, name, metraz, kolor, liczba_okien):
        # uzupełnic inicjalizator
        self.__name = name
        self.__metraz = metraz
        self.__kolor = kolor
        self.__liczba_okien = liczba_okien

    # dopisac metody wyswietl...

    def wyswietl_name(self):
        print(f"Name {self.__name}")

    def wyswietl_metraz(self):
        print(f"Metraż {self.__metraz} m2")

    def wyswietl_kolor(self):
        print(f"Kolor {self.__kolor}")

    def wyswietl_okna(self):
        print(f"Okna {self.__liczba_okien} szt")

    def zmien_metraz(self):
        wyn = int(input("Podaj nowy metraż"))
        self.__metraz = wyn
        self.wyswietl_metraz()

    def zmien_okna(self):
        wyn = int(input("Podaj ilosc okien"))
        self.__liczba_okien = wyn
        self.wyswietl_okna()

    def zmien_kolor(self):
        wyn = input("Podaj kolor")
        self.__kolor = wyn
        self.wyswietl_kolor()


dom1 = Dom("Radek", 300, "biały", 17)
dom1.wyswietl_okna()
# dopisac metody w stylu zmien...
dom1.zmien_metraz()
dom1.zmien_kolor()
