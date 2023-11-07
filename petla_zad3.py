# while - pętla sterowana warunkiem

licznik = 0
while True:
    print("Komunikat!!!")
    licznik += 1
    if licznik > 10:
        break  # przerwanie bieżacej pętli

print(licznik)  # 11
licznik = 0
while licznik < 10:
    print("Komunika2")
    licznik += 1

lista = []
lista2 = []

while True:
    wej = input("Podaj liczbę")  # zraca str()
    if not wej.isnumeric():
        break
    lista.append(wej)
    lista2.append(int(wej))

print(lista)
print(lista2)
# ['1', '2', '3', '4', '5', '6', '7', '8']  - lista stringow
# [1, 2, 3, 4, 5, 6, 7, 8]  - lista intow
