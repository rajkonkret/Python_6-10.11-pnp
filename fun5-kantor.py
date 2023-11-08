# storzenie funkcji kantor
# kantor ma dziąc tak, ze mamy dwie osoby
# danego dnia dana osoba umie wyieniac tylko jeden typ waluty
# zrobic z wykorzystaniem funkcji wewnetrzych
# kantor
# dwie wewnetrzne funkcje (usd, eur)

def kantor(waluta):
    print("Uruchomienie kantoru")

    def usd(kwota=0):
        print(f"Wymieniam {kwota} dol = {kwota * 4.13} pln")

    def eur(kwota=0):
        print(f"Wymieniam {kwota} eur = {kwota * 4.53} pln")

    if waluta.lower().replace(" ", "") == 'eur':
        return eur
    else:
        return usd


kantor_eur = kantor('eur')
kantor_eur()  # Wymieniam eur
# dodac mozliwosc przekazania kwoty do wymiany
# ładnie wyswietlicnp.: wymiam 100 eur na 450 pln
kantor_eur(1000)
# Uruchomienie kantoru
# Wymieniam 0 eur = 0.0 pln
# Wymieniam 1000 eur = 4530.0 pln

kantor_usd = kantor('usd')
kantor_usd(10000)
# Uruchomienie kantoru
# Wymieniam 10000 dol = 41300.0 pln