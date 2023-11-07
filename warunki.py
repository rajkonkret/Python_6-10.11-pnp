# warunki
# uzelazniaja działanie programu na podstawie warunku
# if - instrukcja sterowania przepływem programu

odp = True
if odp:
    print("Brawo")  # gdy spełniony warunek
else:
    print('Ucz się dalej')  # w przeciwnym przypadku

print("Idę dalej")
# Brawo
# Idę dalej

# podatek = 0.9
# zarobki = int(input("Podaj dochód"))
# if zarobki < 10000:
#     podatek = 0.0
# elif zarobki < 30000:
#     podatek = 0.2
# elif zarobki < 100000:
#     podatek = 0.4
# else:
#     podatek = 0.9
# print(f"Płacisz {zarobki * podatek} podatku")
# # dla przedziału 10000 do 29999 ustawic podatek = 0.2
# # kolejnosc warunków ma znaczenie

suma_zam = 100
if suma_zam > 150:
    rabacik = 25
else:
    rabacik = 0

print(f"Rabacik wynosi: {rabacik}")
# suma_zam = 100
rabat = 25 if suma_zam > 150 else 0
print(f"Rabat wynosi: {rabat}")
# Rabacik wynosi: 0
# Rabat wynosi: 0

# zasymulujemy system zbierania logow
# w zaleznosci od systemu i od logu to my bedziemy mieli rózny komunikat

lista_bledow = []
alert_system = "console"
error = "inny"
error_message = "Stało się coś strasznego"

# gdy system email - wywietlic ten nasz komunikat
if alert_system == 'email':
    print(error_message)
elif alert_system == 'console':
    if error == 'medium':
        lista_bledow.append("ostrzeżenie")
    elif error == 'critical':
        lista_bledow.append("krytyczny")
    else:
        lista_bledow.append("inny")
print(lista_bledow)
# 11:30
