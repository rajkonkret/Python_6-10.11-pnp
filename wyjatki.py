# napisac program kalkulator z wykorzystaniem pętli while True jako głównej pętli programu
# menu z dostepnymi działaniami
# pobrac wybrana opcje
# pobrac od uzytkownika liczby
# wyswietlic wynik
# dodac sposób wyjscia z programu

while True:
    print("""
    1. Dodawanie
    2. Odejmowanie
    3. Mnożenie
    4. Dzielenie
    5. Koniec""")

    odp = input('podaj wybraną opcję')  # zwraca str()

    if odp >= '5':
        break
    try:
        a = float(input("Podaj pierwszą liczbę"))
        b = float(input("Podaj drugą liczbę"))

        if odp == '1':
            print(f"Wynik dodawania {a} + {b} = {a + b}")
        elif odp == "2":
            print(f"Wynik odejmowania {a} - {b} = {a - b}")
        elif odp == "3":
            print(f"Wynik mnozenia {a} * {b} = {a * b}")
        elif odp == "4":
            print(f"Wynik dzielenia {a} / {b} = {a / b}")
        else:
            print("Nie znam takiego działania")

    except ZeroDivisionError:
        print("Nie dziel przez zero!!!")
    except ValueError:
        print("Bład wartości")
    except TypeError:
        print("Błąd typu")
    except Exception as e:  # pozostałe wyjątki
        print("Wystąpił bład", e)
    else:  # wykona się tylko, gdy nie wystąpił błąd
        print("operacja zakończyłą się pomyślnie")
    finally:
        print("To wykona się zawsze")
        print("Zakończyłem oblicznia")

# print(f"Używamy wersji Python {wersja:.2f}")  # Używamy wersji Python 3.90
# round() print(round(4.56777, 2))
# try - except [else, finally]
# praca domowa: spróbowac zrobic to za pomocą case
