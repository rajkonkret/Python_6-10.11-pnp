# bazy danych
# nosql, sql
# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")
except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")

