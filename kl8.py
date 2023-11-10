# klasa/metoda abstrakcyjna
from abc import ABC, abstractmethod


class Ptak(ABC):
    """
    Klasa opisująca ptaka w Pythonie
    """

    def __init__(self, gatunek, szybkosc):
        self.gatunek = gatunek
        self.szybkosc = szybkosc

    def latam(self):
        print("Tu", self.gatunek, "Lecę z szybkością", self.szybkosc)

    @abstractmethod
    def wydaj_odglos(self):
        pass


class Kura(Ptak):
    def __init__(self, gatunek):
        super().__init__(gatunek, 0)

    def latam(self):
        print("Tu", self.gatunek, "Ja nie latam")

    def dziobanie(self):
        print("Idę podziobać")

    def wydaj_odglos(self):
        print("Ko ko ko ko")


class Orzel(Ptak):

    def poluj(self):
        print("Robię polowanie")

    # gdybysmy nie nadpisali tej metody
    # TypeError: Can't instantiate abstract class Orzel with abstract method wydaj_odglos
    def wydaj_odglos(self):
        print('kiiiir ki-er')


# po oznaczeniu kalsy i metody jako abstrakcyjne
# nie mozna stworzyc obiektu takiej klasy
# TypeError: Can't instantiate abstract class Ptak with abstract method wydaj_odglos
# or1 = Ptak("Orzeł", 25)
# or1.latam()
# kur1 = Ptak("Kura", 0)
# kur1.latam()
# or1.wydaj_odglos()
# kur1.wydaj_odglos()

kur2 = Kura("Kura")
kur2.latam()  # Tu Kura Ja nie latam
kur2.dziobanie()
or2 = Orzel("Orzel", 48)
or2.latam()
or2.poluj()
or2.wydaj_odglos()
kur2.wydaj_odglos()
