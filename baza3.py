# bazy danych
# nosql, sql
# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    with open('tables.sql', 'r') as file:
        sql_script = file.read()

    cursor.executescript(sql_script)  # wykonanie wczytanego skryptu na bazie danych

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
# Baza zostałą podłączona
# Baza została zamknięta
