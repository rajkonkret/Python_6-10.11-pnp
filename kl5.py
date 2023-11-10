# dziedziczenie
# przejmowanie i/lub rozszerzanie własciwosc klasy wyzszej w naszej klasie
class Pojazd:
    """
    Klasa opsująca pojazd
    """

    def __init__(self, kolor):
        self.kolor = kolor

    def info(self):
        print(f"Kolor {self.kolor}")


class Samochod(Pojazd):  # klasa dziedziczy po klasie pojazd
    """
    samochod
    """

    def __init__(self, kolor, marka):
        super().__init__(kolor)
        self.marka = marka

    def info(self):
        super().info()  # mozemy uzyc metody z klasy wyzszej
        print(f"Marka {self.marka}")


poj1 = Pojazd("biały")
poj1.info()  # Kolor biały
poj2 = Samochod("biały", "Ferrari")
poj2.info()

lista = [poj1, poj2]
for i in lista:
    i.info()

print(poj1.__doc__)  # wyswietlenie dokumentacji
