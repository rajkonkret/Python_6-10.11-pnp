class MyException(Exception):
    def __init__(self, message):
        super().__init__(message)


try:
    # print(6 / 0)
    # raise TypeError('Bład typu')
    raise MyException("komentarz")  # MyException: komentarz
except ZeroDivisionError:
    print("Nie dziel przez zero")
except TypeError:
    print("Bład typu")
except MyException:
    print("Wystąpił wyjątek MyException")
# 11:15
