import sqlite3

def main():
    conn = sqlite3.connect("my_sql.db")
    cur = conn.cursor()
    # Создание таблицы с полями
    #cur.execute("""CREATE TABLE Customers(CustomerID INTEGER PRIMARY KEY NOT NULL, Name TEXT, Email TEXT)""")

    # Создание данных в таблице
    cur.execute("""INSERT INTO Customers (Name, Email)
                VALUES ("ser", "ser333@yandex.ru"),
                        ("vaccv", "vaccv333@yandex.ru")""")

    # Получение данныи из таблицы
    cur.execute("SELECT * FROM Customers")
    sel = cur.fetchall()

    for el in sel:
        print(f"ID {el[0]}, Name:{el[1]}, Email--{el[2]}")


    conn.commit()
    conn.close()


if __name__ == "__main__":
    main()
