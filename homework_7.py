import sqlite3

connect = sqlite3.connect("hw.db")
cursor = connect.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS products(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            product_title VARCHAR (200) NOT NULL,
            price FLOAT (6, 3) DEFAULT 0.0,
            quantity INTEGER NOT NULL DEFAULT 0)""")

def add_products():
    product_name = input("Введите название продукта: ")
    price_product = float(input("Введите цену продукта (в сомах): "))
    quantity_products = int(input("Введите количество данного продукта: "))

    cursor.execute("""INSERT INTO products (product_title, price, quantity)
                    VALUES (?, ?, ?)""", (product_name, price_product, quantity_products))

    connect.commit()

add_products()

def some_thing():
    cursor.execute("SELECT product_title, price FROM products")
    thing = cursor.fetchall()
    print(thing)

some_thing()