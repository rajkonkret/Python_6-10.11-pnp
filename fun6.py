# napisanie funkcji, ktora oblicza srednia (np.: ocen)
def liczby(name=None, *cyfry):  # dowolna ilosc argumentów typu pozycyjnego
    # print(cyfry)
    suma = 0
    count = len(cyfry)
    try:
        for c in cyfry:
            suma += c  # suma = suma + c
        print(f"Średnia wynosi {suma / count}")
    except ZeroDivisionError:
        print(f"Uczeń {name} nie ma ocen")
    except Exception as e:
        print("Bład", e)


def liczby2(*cyfry, name=None):
    print(cyfry)
    print(name)


liczby()
liczby("Adam", 1)
liczby("Tomek", 1, 2, 3, 4, 5, 6, 7)  # ctrl alt l
liczby("a", "a")  # Bład unsupported operand type(s) for +=: 'int' and 'str'

liczby2(1, 2, 3, 4, 5)
# (1, 2, 3, 4, 5)
# None
liczby2("Zenek", 1, 2, 3, 4, 5)
# ('Zenek', 1, 2, 3, 4, 5)
# None
liczby2(1, 2, name="Zenek")
# (1, 2)
# Zenek
