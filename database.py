import sqlite3


db = sqlite3.connect('data_base.db', check_same_thread=False)
query = db.cursor()


def create_db():
    # Таблица Персонаж
    query.execute("""CREATE TABLE IF NOT EXISTS character(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL);
        """)
    db.commit()
    # Таблица Вид товара
    query.execute("""CREATE TABLE IF NOT EXISTS product_type(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL);
            """)
    db.commit()
    # Таблица Товар
    query.execute("""CREATE TABLE IF NOT EXISTS product(
        id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        name TEXT NOT NULL,
        link TEXT NOT NULL,
        char TEXT NOT NULL,
        type TEXT NOT NULL,
        FOREIGN KEY (char) references character(name),
        FOREIGN KEY (type) references product_type(name));
        """)
    db.commit()
