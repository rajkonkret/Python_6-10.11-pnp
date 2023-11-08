# funkcja - wydzielony fragment kodu, który można wykonac wielokrotnie

a = 6  # zmienne globalne(w głownym scope)
b = 7


# deklaracja funkcji - zapisuje gdzie w pamięci ma funkcje
# funkcja musi byc zdeklarowane przed użyciem
# dane ze scopa głownego (wyzszego) beda widoczne
def dodaj():  # funkcja bezargumentowa
    c = 7  # c nie bedzie widoczne poza ta funkcja (w w yzszym scopie(zakresie)) - zmienna lokalna w funkcji
    print(a + b)


def dodaj2(a, b):  # a,b zadeklarowane w funkci (lokalne) - obowiązkowe do przekazania
    print(a + b)


def odejmij(a, b, c=0):  # c=0 parametr z wartością domyslna
    print(a - b - c)


# nazwa funkcji, nawiasy (), ewnetualnie w nawiasach argumenty
dodaj()  # 13 - miejsce wykonania funkcji
dodaj2(8, 9)  # 17
odejmij(1, 2, 3)  # wywołanie z c=3
odejmij(1, 2)  # wywołanie z domyslnym c=0
odejmij(b=9, a=8)  # argumenty przekazane po nazwie
odejmij(c=9, b=3, a=9)
dodaj2(b=-8, a=9)

# print(dodaj() + odejmij(6, 9))  # TypeError: unsupported operand type(s) for +: 'NoneType' and 'NoneType'
print(dodaj())  # None
