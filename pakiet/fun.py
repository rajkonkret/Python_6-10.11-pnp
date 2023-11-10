def powitanie():
    print("Cześć")


def info():
    print("Jestem funkcją info z pakietu pakiet z pliku fun")


print(__name__)
if __name__ == '__main__':
    powitanie()
    info()

# Cześć
# Jestem funkcją info z pakietu pakiet z pliku fun
