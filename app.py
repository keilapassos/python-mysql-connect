from flask import Flask, jsonify, request
import mysql.connector
import os
import dotenv 

dotenv.load_dotenv()

app = Flask(__name__)
app.config["JSON_SORT_KEYS"] = False

connection = mysql.connector.connect(
        host=os.getenv('HOST'), 
        user='root', 
        password=os.getenv('PASSWORD'), 
        port=os.getenv('PORT'), 
    )

cursor = connection.cursor()


def database():
    try:

        cursor.execute("CREATE DATABASE IF NOT EXISTS mydatabase")
        
        cursor.execute("""USE mydatabase;""")
        
        cursor.execute("""CREATE TABLE IF NOT EXISTS users(
            id int not null auto_increment,
            nome varchar(110),
            cpf varchar(11),
            data_nascimento date,
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
    data = request.json

    if not 'nacionalidade' in data:
        data['nacionalidade'] = 'default'
    else:
        data['nacionalidade']


    users_keys = ["nome", "cpf", "data_nascimento", "sexo", "peso", "altura", "nacionalidade"]    
    
    try:
    
        cursor.execute(f"""INSERT INTO users
            (id, nome, cpf, data_nascimento, sexo, peso, altura, nacionalidade)
            values
            (default, '{data['nome']}', '{data['cpf']}', '{data['data_nascimento']}', '{data['sexo']}', '{data['peso']}', '{data['altura']}', {data['nacionalidade']})
        """)

        connection.commit()

        return jsonify(data)
    except:
        return {"accepted keys": [key for key in users_keys if key not in users_keys]}


@app.get("/users")
def get_all_users():

    users_keys = ["id", "nome", "cpf", "data_nascimento", "sexo", "peso", "altura", "nacionalidade"]

    cursor.execute("SELECT * FROM users;")  
    users = cursor.fetchall()
    
    result = [dict(zip(users_keys, user)) for user in users]

    return jsonify(result)


@app.get("/users/<int:id>")
def get_user(id):

    user_keys = ["id", "nome", "cpf", "data_nascimento", "sexo", "peso", "altura", "nacionalidade"]

    cursor.execute(f"SELECT * FROM users WHERE id = {id};")  

    user = cursor.fetchall()

    if not user:
        return jsonify({"msg": "user not found"}), 404
    
    result = [dict(zip(user_keys, user)) for user in user]

    return jsonify({"data": result}), 200



@app.patch("/users/<int:id>")
def update_user(id):

    user_keys = ["id", "nome", "cpf", "data_nascimento", "sexo", "peso", "altura", "nacionalidade"]

    cursor.execute(f"SELECT * FROM users WHERE id = {id};")  

    user = cursor.fetchall()
    
    if not user:
        return jsonify({"msg": "user not found"}), 404
        
    data = request.json

    for key in data:
        if key == 'id':
            return {"msg": "unavailable field, id can not be changed"}, 400
        if key not in user_keys:            
            return ({"available keys": [key for key in user_keys]})
        cursor.execute(f"UPDATE users SET {key} = '{data[key]}' WHERE id = {id};")  

    connection.commit()

    cursor.execute(f"SELECT * FROM users WHERE id = {id};")  

    user = cursor.fetchall()

    result = [dict(zip(user_keys, user)) for user in user]

    return jsonify({"data": result}), 200
    

@app.delete("/users/<int:id>")
def delete_user(id):
    cursor.execute(f"SELECT * FROM users WHERE id = {id};")  

    user = cursor.fetchall()
    
    if not user:
        return jsonify({"msg": "user not found"}), 404
    
    cursor.execute(f"DELETE FROM users WHERE id = {id};")  

    connection.commit()

    return jsonify({"msg": "deleted successfully"}), 200
    
