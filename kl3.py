class Car:
    """
    Klasa opisująca samochód
    """

    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.__predkosc = 0  # pole jest prywatne

    def gaz(self):
        self.__predkosc += 10
        self.__zmien_bieg()

    def licznik(self):
        print(f"Jedziesz z szybkością {self.__predkosc} km/h")

    def hamuj(self):
        self.__predkosc -= 10

    def __zmien_bieg(self):  # metoda prywatna
        print("Zmiana biegu")


car1 = Car("Fiat", 2023)
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
car1.gaz()
# po oznaczeniu pola jako prywatne dostajemy bład
# print(car1.__predkosc)  # 50  AttributeError: 'Car' object has no attribute '__predkosc'.
# Did you mean: '_Car__predkosc'?

car1.licznik()  # Jedziesz z szybkością 50 km/h
# car1.__predkosc = 200  # stworzylismy dodakowe pole , przypadkowo o tej samej nazwie
car1.licznik()  # Jedziesz z szybkością 200 km/h
# car1.__predkosc = 0
car1.licznik()  # Jedziesz z szybkością 0 km/h
# print(car1.__predkosc)
# dopisac metode hamuj()
car1.hamuj()
car1.hamuj()
car1.hamuj()
car1.licznik()  # Jedziesz z szybkością 20 km/h
