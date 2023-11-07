# match case - instrukcja sterowania przepływem programu
lista = []
lang = input("Podaj znany Ci język programowania")

match lang.lower().replace(" ", ""):
    case "python":
        lista.append(lang)
    case "java":
        lista.append(lang)
    case "c++":
        lista.append(lang)
    case _:  # domyslne zachowania (odpowiednik else)
        print("Nie znam takiego języka")

print(f"Lista odpowiedzi {lista}")
