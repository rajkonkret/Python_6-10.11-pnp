# uzycie zmiennych globalnych wewnatrz i na zewnatrz funkcji
a = 10
b = 10


def dodaj():
    a = 6  # zmienne lokalne, bez wpływu na zmienne globalne, zakres w obrębie tej funkcji
    b = 7
    print(a + b)


def dodaj2():
    print(a + b)


def dodaj3():
    global a  # wewnatrz funkcji uzyje zmiennej globalnej,
    # kazda zmiana w funkcji wartosci tej zmiennej zmienia wartośc tej zmiennej globalnie
    a = 6
    b = 7
    print(a + b)


print(f"Zmienna a z góry (globalna) {a}")
dodaj()
print(f"Zmienna a z góry (globalna) {a}")  # Zmienna a z góry (globalna) 10
dodaj2()  # 20
print(f"Zmienna a z góry (globalna) {a}")  # Zmienna a z góry (globalna) 10
dodaj3()
print(f"Zmienna a z góry (globalna) {a}")  # Zmienna a z góry (globalna) 6
dodaj2()  # 16
