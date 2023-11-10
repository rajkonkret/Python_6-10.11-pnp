# wielodziedziczenie
#  w pythonie mozemy dziedziczyc na raz po wielu klasach

class A:
    def method(self):
        print('Metoda z klasy A')


class B:
    def method(self):
        print("Metoda z kalsy B")

    def method2(self):
        print("Metoda 2 z klasy B")


class C(A, B):  # kolejnosc ma znaczenie
    """
    klasa C - dziedziczy po klasach A i B
    """

    def method(self):
        print('Metoda z klasy C')  # Metoda z klasy C
        super().method()  # Metoda z klasy A
        B.method(self)  # wyrazne wskazanie, ze chcemy metody z klasy B, przekazujemy obiekt do metody


a = A()
a.method()

b = B()
b.method()
c = C()
c.method()  # Metoda z klasy A, gdy nadpiszemy metode w klasie C -> Metoda z klasy C
# Metoda z klasy C
# Metoda z klasy A
# Metoda z kalsy B
print(C.__mro__)
# ___mro__ - kolejnosc rozwiazywania nazw
# (<class '__main__.C'>, <class '__main__.A'>, <class '__main__.B'>, <class 'object'>)
c.method2()  # Metoda 2 z klasy B
# Metoda z klasy C
# Metoda z klasy A
# Metoda z kalsy B