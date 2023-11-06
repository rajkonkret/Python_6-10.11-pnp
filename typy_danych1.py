wiek = 47  # int
rok = 2023  # int
temp = 36.6  # float
wiek2 = 37.5
# wiek = 37,5   to nie jest liczba

print(wiek)
print(type(wiek))
print(wiek2)
print(type(wiek2))
print(rok)
print(type(rok))
print(temp)
print(type(temp))
# 47
# <class 'int'>
# 37.5
# <class 'float'>
# 2023
# <class 'int'>
# 36.6
# <class 'float'>
print(5 * "Radek")  # RadekRadekRadekRadekRadek

print(wiek + rok)
print(wiek * rok)
print(wiek - rok)
print(wiek / rok)  # wynik dzielania jest typu float
# 2070
# 95081
# -1976
# 0.023232822540781017
print(wiek // rok)  # cześć całkowita z dzielenia
print(wiek % rok)  # reszta z dzielenia czyli modulo  47

print(5 % 2)  # 1 bo 2 * 2 = 4 + 1 = 5
print(wiek ** rok)
print(54 - 5 * 43 + 4 / 2 + 4 / 2)
print(54 - 5 * 43 + (4 / 2 + 4) / 2)
# -157.0
# -158.0
print(0.2 + 0.8)  # 1.0
print(0.2 + 0.7)  # 0.8999999999999999
# występuje błąd zaokraglenia
# 1 X 10 ^56
print(f"{0.2 + 0.7:.1f}")  # 0.9
print(f"Sprawdzenie zmiennej {temp} {wiek}")
print(f"""
{wiek}
    {temp}
""")

# typ logiczny
# True False
czy_znasz_Python = False
print(czy_znasz_Python)  # True
print(type(czy_znasz_Python))  # <class 'bool'> typ logiczny
print(int(czy_znasz_Python))  # 1 - True, 0 - False
x = 1
print(bool(x))  # bool() - zamiana na typ logiczny, 1=True
x = 100
print(bool(x))  # True
x = -10
print(bool(x))  # True
x = 0
print(bool(x))  # False
x = ''
print(bool(x))  # False
x = "Radek"
print(bool(x))  # True
x = None
print(bool(x))  # False

# działąnia logiczny
# and - i
print(True and True)
print(True and False)
print(False and True)
print(False and False)
# True
# False
# False
# False
# or - lub
print(True or True)
print(True or False)
print(False or True)
print(False or False)
# True
# True
# True
# False

# not - negacja
print(not False)
print(not True)
# True
# False

x = 1
print(not x == 1)  # False

a = 8
b = 7

print(f"Porównanie {a} > {b}", a > b)
print(f"Porównanie {a} < {b}", a < b)
print(f"Porównanie {a} == {b}", a == b)  # == porównanie, czy a równa się b
print(f"Porównanie {a} != {b}", a != b)  # czy różne
print(f"Porównanie {a} >= {b}", a >= b)
print(f"Porównanie {a} <= {b}", a <= b)
# Porównanie 8 > 7 True
# Porównanie 8 < 7 False
# Porównanie 8 == 7 False
# Porównanie 8 != 7 True
# Porównanie 8 >= 7 True
# Porównanie 8 <= 7 False
# stackoverflow
# chatgpt
