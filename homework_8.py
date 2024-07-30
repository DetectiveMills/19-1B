import sqlite3


connect = sqlite3.connect("bank.db")
cursor = connect.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS clients(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) NOT NULL,
        age INTEGER NOT NULL,
        address VARCHAR(50) NOT NULL, 
        email VARCHAR(50) NOT NULL UNIQUE,
        balance DOUBLE DEFAULT 0.0,
        is_vip BOOLEAN DEFAULT False
        )""")

cursor.execute("""
CREATE TABLE IF NOT EXISTS vip_client(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        full_name VARCHAR(50) NOT NULL
        )""")



class BankSystem:
    def __init__(self):
        self.full_name = None
        self.age = None
        self.address = None
        self.email = "@gmail.com"
        self.balance = 0.0
        self.is_vip = False


    def register(self):
        user_full_name = input("Введите свое имя: ")
        user_age = input("Введите свой возраст: ")
        user_address = input("Введите свой адрес: ")
        user_email = input("Введите свою почту: ")


        cursor.execute("SELECT email FROM clients WHERE email = ?", (user_email,))
        client = cursor.fetchone()
        
        if client:
            print("\nПользователь с таким email уже зарегистрирован")

        else:
            cursor.execute("""
            INSERT INTO clients (full_name, age, address, email)
            VALUES (?, ?, ?, ?)""", (user_full_name, user_age, user_address, user_email))
            print("\nРегистрация успешна!")

        connect.commit()


    def chek_balance(self):
        user_id = int(input("\nВведите id счёта: "))
        cursor.execute("SELECT balance FROM clients WHERE id = ?", (user_id,))
        clients_balance = cursor.fetchall()
        print(clients_balance)


    def vip_client_add(self):
        cursor.execute("SELECT * FROM clients WHERE balance >= 200000")
        if_1 = cursor.fetchall()

        for client in if_1:
            user_id = client[0]
            user_full_name = client[1]

            cursor.execute("SELECT id FROM vip_client WHERE full_name = ?", (user_full_name,))
            vip_client = cursor.fetchone()
            
            if not vip_client:
                cursor.execute("""UPDATE clients SET 
                        is_vip = ? WHERE id = ?""", (True, user_id))
                
                cursor.execute(f"""INSERT INTO vip_client 
                            (full_name) VALUES ('{user_full_name}')""")
                connect.commit()

            else:
                pass

    def take_off_balance(self):
        while True:
            user_id = int(input("\nВведите id клиента: "))
            user_balance = float(input("Введите сумму: "))

            cursor.execute(f"SELECT balance FROM clients WHERE balance >= {user_balance}")
            client_balance = cursor.fetchone()

            cursor.execute(f"SELECT id FROM clients WHERE id = {user_id}")
            client = cursor.fetchone()

            if client_balance and client:
                cursor.execute("""UPDATE clients SET 
                            balance = balance - ? WHERE id = ?""", (user_balance, user_id))
                connect.commit()

                cursor.execute("SELECT balance FROM clients WHERE id = ?", (user_id,))
                clients_balance = cursor.fetchall()
                print(f"\nСчет {user_id}: снято {user_balance}. Новый баланс: {clients_balance}")
                break

            elif client:
                print("\nНедостаточно средств на счете.")
                continue

            else:
                print("\nТакого счёта нет в нашем банке!")
                break
    
    
    def update_balance(self):
        user_id = int(input("\nВведите id клиента: "))
        user_balance = float(input("Введите сумму: "))
        cursor.execute(f"SELECT id, full_name FROM clients WHERE id = {user_id}")
        client = cursor.fetchone()

        if client:
            cursor.execute("""UPDATE clients SET 
                    balance = balance + ? WHERE id = ?""", (user_balance, user_id))
            connect.commit()

            cursor.execute("SELECT balance FROM clients WHERE id = ?", (user_id,))
            clients_balance = cursor.fetchall()
            print(f"Счет {user_id}: пополнено {user_balance}. Новый баланс: {clients_balance}")

        else:
            print("\nТакого счёта нет в нашем банке!")
    
    
    def main(self):
        while True:
            self.vip_client_add()
            print("\nВыберите действие: ")
            print("0 - выйти, 1 - регистрация, 2 - проверить баланс,  \n3 - пополнить баланс, 4 - снять деньги:")
            command = int(input(": "))
            if command == 0:
                break
            elif command == 1:
                self.register()
            elif command == 2:
                self.chek_balance()
            elif command == 3:
                self.update_balance()
            elif command == 4:
                self.take_off_balance()


client = BankSystem()
client.main()