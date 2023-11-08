# praca z plikami
# kontekst menadżer
# with
# Character Meaning
#     --------- ---------------------------------------------------------------
#     'r'       open for reading (default)
#     'w'       open for writing, truncating the file first
#     'x'       create a new file and open it for writing
#     'a'       open for writing, appending to the end of the file if it exists
#     'b'       binary mode
#     't'       text mode (default)
#     '+'       open a disk file for updating (reading and writing)
#     ========= ===============================================================
with open('test.log', 'w', encoding='utf-8') as fh:  # filehandler
    fh.write("Powitanie\n")
    fh.write("kolejne\n")
    fh.write("Jeszcze jedno\n")

# w - kasuje plik gdy istnieje i tworzy na nowo. nie ma błedu
with open('test.log', 'wt', encoding='utf-8') as fh:
    fh.write("Radek\n")

# Dla x, gdy plik istnieje dostaniemy bład: FileExistsError: [Errno 17] File exists: 'test.log'
# with open('test.log', 'xt') as fh:
#     fh.write("Radek\n")

with open('test.log', 'a', encoding='utf-8') as file:
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dodane\n")
    file.write("Dośdane\n")
# file.write("")  # ValueError: I/O operation on closed file.


with open('test.log', 'r', encoding='utf-8') as f:
    lines = f.read()

print(lines)

# Radek
# Dodane
# Dodane
# Dodane
# Dośdane
