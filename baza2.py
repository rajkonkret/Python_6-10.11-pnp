# bazy danych
# nosql, sql
# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    # ZAPISANE W JEZYKU SQL
    query = '''
    CREATE TABLE IF NOT EXISTS developers(
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    joining_date DATETIME,
    salary REAL NOT NULL);
    '''

    insert = '''
    INSERT INTO developers (id, name,email,salary) VALUES (1,'Radek','raj@wp.pl',5000);
    '''
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")

    # sql_connection.execute(query)
    sql_connection.execute(insert)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
# 13:15

