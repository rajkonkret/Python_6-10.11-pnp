# funkcje zagniezdzone
def fun1X():
    print("To jest fun1")

    def fun2():  # deklaracja fun2
        print("To jest fun2")

    return fun2  # zwracamy tylko adres w pamieci, gdzie jest umieszczona funkcja


print(fun1X())  # <function fun1.<locals>.fun2 at 0x0000025446F88D60>
print(type(fun1X()))  # <class 'function'>

xFun = fun1X()
print(xFun)  # <function fun1.<locals>.fun2 at 0x0000017DA4B38D60>
xFun()  # To jest fun2
# 13:15
