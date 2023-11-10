class Pracownik:
    def __init__(self, imie, nazwisko, pensja):
        self.imie = imie
        self.nazwisko = nazwisko
        self.pensja = pensja

    def przedstaw_sie(self):
        print(f"Cześć, jestem {self.imie} {self.nazwisko}")

    def oblicz_pensje(self):
        return self.pensja


class Manager(Pracownik):
    def __init__(self, imie, nazwisko, pensja, premia):
        super().__init__(imie, nazwisko, pensja)
        self.premia = premia

    def oblicz_pensje(self):
        return self.pensja + self.premia


pracownik = Pracownik("Jan", "Kowalski", 10000)
pracownik.przedstaw_sie()  # Cześć, jestem Jan Kowalski
pen_prac = pracownik.oblicz_pensje()
print(f"{pracownik.imie} {pracownik.nazwisko}. Zarabiam {pen_prac} brutto")
# stworzyc klase Manager
#
manago =  Manager("Anna", "Nowak", 10000, 3500)
manago.przedstaw_sie()
pen_manago = manago.oblicz_pensje()
print(f"{manago.imie} {manago.nazwisko}. Zarabiam {pen_manago} brutto")

# Cześć, jestem Jan Kowalski
# Jan Kowalski. Zarabiam 10000 brutto
# Cześć, jestem Anna Nowak
# Anna Nowak. Zarabiam 13500 brutto
