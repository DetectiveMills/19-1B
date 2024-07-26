import sqlite3

connect = sqlite3.connect("Back_19_1.db")
cursor = connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS students(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            full_name VARCHAR (50) NOT NULL,
            hobby TEXT DEFAULT NULL,
            phone_number INT NOT NULL DEFAULT 996,
            birth_date DATE,
            mark DOUBLE (5, 2) DEFAULT 0.0,
            is_mentor BOOLEAN DEFAULT False    
               )""")


def add_student():
    user_full_name = input("Введите имя: ")
    user_hobby = input("Введите хобби: ")
    user_phone_number = int(input("Введите номер телефона: "))
    user_birth_date = input("Введите дату рождения: ")


    cursor.execute(f"""INSERT INTO students
            (full_name, hobby, phone_number, birth_date)
                VALUES ('{user_full_name}', '{user_hobby}', {user_phone_number}, '{user_birth_date}')""")
    
    # cursor.execute("""INSERT INTO students
    #                (full_name, hobby, phone_number, birth_date)
    #                VALUES ('?', '?', ?, '?')""", user_full_name, user_hobby, user_phone_number, user_birth_date)
    
    connect.commit() 

add_student()

def all_student():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    print(students)

all_student()