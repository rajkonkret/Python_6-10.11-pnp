# bazy danych
# nosql, sql
# sqlite3 - baza sql w jednym pliku, moze byc przechowywana w pamieci
import sqlite3

try:
    sql_connection = sqlite3.connect('sqlite_python.db')
    cursor = sql_connection.cursor()
    print("Baza zostałą podłączona")
    # CRUD -> C
    insert = '''
    INSERT INTO software (id, name, price) VALUES (1, 'Python', 100);
    '''
    # CRUD -> R
    select = '''
    SELECT * FROM software WHERE id=1;
    '''
    for row in cursor.execute(select):
        print(row)  # (1, 'Python', 100.0)
    # CRUD -> U
    update = '''
    UPDATE software SET price = 2000 WHERE id=1;
    '''

    # CRUD -> D
    delete = '''
    DELETE FROM software WHERE id=1;
    '''

    # cursor.execute(insert)
    # sql_connection.commit()
    # cursor.execute(update)
    # sql_connection.commit()
    cursor.execute(delete)
    sql_connection.commit()

except sqlite3.Error as e:
    print("Bład podczas podłaczania bazy danych", e)
finally:  # wykonuje sie zawsze
    if sql_connection:
        sql_connection.close()
        print("Baza została zamknięta")
