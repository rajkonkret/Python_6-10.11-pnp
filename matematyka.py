import math
import sys

# wypisanie argumentow z jakimi został uruchomiony program
print(sys.argv)  # ['C:\\Users\\CSComarch\\PycharmProjects\\Python_6-10.11-pnp\\matematyka.py']
# po uruchomieniu programu z parametrem mamy wypisany ten parametr
# python .\matematyka.py 1
# ['.\\matematyka.py', '1']

pi = math.pi
print(pi)  # 3.141592653589793

print(math.sqrt(625))  # 25.0
print(math.cos(90))
# (venv) PS C:\Users\CSComarch\PycharmProjects\Python_6-10.11-pnp> python .\matematyka.py 1 2 3 4 5
# ['.\\matematyka.py', '1', '2', '3', '4', '5']

print(dir())
# ['__annotations__', '__builtins__', '__cached__', '__doc__',
# '__file__', '__loader__', '__name__', '__package__', '__spec__', 'math', 'pi', 'sys']
print([x for x in dir() if not x.startswith('_')])
# ['math', 'pi', 'sys'] wypisał uzyte zmienne
