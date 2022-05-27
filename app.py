from flask import Flask
import mysql.connector

app = Flask(__name__)


connection = mysql.connector.connect(host='localhost', user='root', password='1234', port='3306', db='mysql')

cursor = connection.cursor()

def database():
    try:
        print("1. CREATE DATABASE IF NOT EXISTS mydatabase...\n")
        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        
        print("2. USE mydatabase...\n")
        cursor.execute("""USE mydatabase;""")

        print("3. CREATE TABLE IF NOT EXISTS users...\n")
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id int not null auto_increment,
            nome varchar(110),
            cpf varchar(11),
            dt_nascimento date,
            sexo enum('F', 'M'),
            peso decimal(5, 2),
            altura decimal(3, 2),
            nacionalidade varchar(20) default 'Brasileira',
            primary key(id))
        ;""")
        
        print("4. INSERT INTO users...\n")
        cursor.execute("""INSERT INTO users
            (id, nome, cpf, dt_nascimento, sexo, peso, altura, nacionalidade)
            values
            (default, 'Maria', '11111111111', '1995-05-11', 'F', '45.62', '1.54', default),
            (default, 'João', '22222222222', '1986-01-26', 'M', '97.85', '1.97', 'Canadense'),
            (default, 'Cléber', '33333333333', '1998-12-12', 'M', '59.04', '1.67', 'Brasileira'),
            (default, 'Lucas', '44444444444', '1995-07-25', 'M', '80.30', '1.81', 'Irlandesa'),
            (default, 'Poliana', '55555555555', '2000-05-22', 'F', '58.37', '1.58', default);
        """)

        print("4. commit users...\n")
        connection.commit()
        # cursor.execute("INSERT INTO customers (name, address) VALUES ('Adrian', 'Tal rua');")
        # cursor.execute("INSERT INTO customers (name, address) VALUES ('Keila', 'Tal rua 2');")

        print("Record inserted successfully into customers table\n")

        # selecionando tudo de pessoas_keila2:
        print("5. SELECT * FROM users...\n")
        cursor.execute("SELECT * FROM users;")   
        # cursor.execute("SELECT * FROM customers;")  

        # result = cursor.fetchall()
        # print(result)
        
        print("6. CLOSING CONNECTION...\n")
        cursor.close()
        connection.close()
        print("MySQL connection is closed")
        return
        
    except:
        print("end of DATABASE")

database()

@app.get("/")
def send_to_home_page():
    return "Home page here"