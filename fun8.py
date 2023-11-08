def allparams(a, b, /, **kwargs):
    print(a)
    print(b)
    print(kwargs)


def allparams2(a, b, /, c):
    print(a, b, c)


def allparams3(a, b, /, c=42, *args, d=256, **kwargs):
    print("a, b", a, b)
    print("c, d", c, d)
    print("args, kwargs", args, kwargs)


allparams(1, 2)
allparams(1, 2, c=8)
# 1
# 2
# {'c': 8}
# dodanie / do argumentów powoduje, ze argumenty z lewej strony musza byc podane jako pozycyjne
# pozostałe wg reguł
# allparams(1, b=2, c=7)  # TypeError: allparams() missing 1 required positional argument: 'b'
allparams(1, 2, b=2, c=3)  # {'b': 2, 'c': 3}
# 1
# 2
# {'b': 2, 'c': 3}
allparams2(1, 2, 3)  # 1 2 3
allparams2(1, 2, c=8)  # 1 2 8

allparams3(1, 2)
allparams3(1, 2, c=67)  # c, d 67 256
# gdy chcemy wrzucic wartosci do args, c musimy podaj pozycyjnie(nie mozna po nazwanych uzywac pozycyjnych)
allparams3(1, 2, 67, 7, 8, 9)  # c, d 67 256, args, kwargs (7, 8, 9) {}
# d musimy podac po nazwie(gdy nie chcemy wartosci domyslnej)
allparams3(1, 2, 67, 7, 8, 9, 11, 12, d=89)  # c, d 67 89, args, kwargs (7, 8, 9, 11, 12) {}
allparams3(1, 2, 67, 7, 8, 9, 11, 12, d=89, e=9)  # c, d 67 89, args, kwargs (7, 8, 9, 11, 12) {}
# a, b 1 2
# c, d 67 89
# args, kwargs (7, 8, 9, 11, 12) {'e': 9}
allparams3(1, 2, a=0)
# a, b 1 2
# c, d 42 256
# args, kwargs () {'a': 0}
