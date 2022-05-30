from flask import Flask, jsonify
import mysql.connector
import os
import dotenv 

dotenv.load_dotenv()

app = Flask(__name__)
# app.config["JSON_SORT_KEYS"] = False

connection = mysql.connector.connect(
        host=os.getenv('HOST'), 
        user='root', 
        password=os.getenv('PASSWORD'), 
        port=os.getenv('PORT'), 
        db=os.getenv('DB')
    )

cursor = connection.cursor()


def database():
    try:
        # cursor = connection.cursor()

        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        
        cursor.execute("""USE mydatabase;""")
        
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

        
    except:
        return {"msg": "database error"}

database()

@app.post("/users")
def create_users():
    # try:
    # cursor = connection.cursor()
    
    cursor.execute("""INSERT INTO users
        (id, nome, cpf, dt_nascimento, sexo, peso, altura, nacionalidade)
        values
        (default, 'Maria', '11111111111', '1995-05-11', 'F', '45.62', '1.54', default),
        (default, 'João', '22222222222', '1986-01-26', 'M', '97.85', '1.97', 'Canadense'),
        (default, 'Cléber', '33333333333', '1998-12-12', 'M', '59.04', '1.67', 'Brasileira'),
        (default, 'Lucas', '44444444444', '1995-07-25', 'M', '80.30', '1.81', 'Irlandesa'),
        (default, 'Poliana', '55555555555', '2000-05-22', 'F', '58.37', '1.58', default);
    """)

    # cursor.execute("""INSERT INTO users
    #     (id, nome, cpf, dt_nascimento, sexo, peso, altura, nacionalidade)
    #     values
    #     (default, '%s', %s, %s, %s, %s, %s, %s);
    # """)

    # commit é usado quando há alterações no banco, como:
    # inserção, deleção e update de dados
    connection.commit()

    return {"msg": "Record inserted successfully into users table"}

@app.get("/")
def get_all_users():

    users_keys = ["id", "nome", "cpf", "dt_nascimento", "sexo", "peso", "altura", "nacionalidade"]

    cursor.execute("SELECT * FROM users;")  
    users = cursor.fetchall()
    
    result = [dict(zip(users_keys, user)) for user in users]

    return jsonify(result)