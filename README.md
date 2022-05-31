Aplicação com proposito de aprendizado: 
 ``` conectando python e mysql com mysql-connect ``` 

<br>

Estou utilizando este projeto para aprender a conectar python a bancos de dados e fazer <strong>CRUD de usuários </strong> (inserção, consultas, atualização e deleção de informações).

A princípio, este projeto será feito apenas com mysql-connect, sem utilizar ORMs.

Passo-a-passo para utilizar esta aplicação:

<br>

1. Clonar o repositório:

```
    git clone https://github.com/keilapassos/python-mysql-connect
```

<br>

2. Abra o diretório do projeto com seu editor de texto, exemplo com VSCode:
```
    cd python-mysql-connect
    code .
```

<br>

3. Criar um ambiente virtual e entrar nele:
    python -m venv venv

```
    source venv/bin/activate
```

4. Copiar ou renomear o .env.example para .env (faça alterações nesse arquivo caso necessário para sua conexão local com mysql)

<br>

5. Baixe as dependências necessárias para o projeto:
```
    pip install -r requirements.txt
```

<br>

6. Rodar a aplicação:
```
    flask run
```

<br><br>

## Acessando rotas/endpoints

Essa aplicação possui 5 endpoits. Sua url base pode ser acessada como http://127.0.0.1:5000 ou http://localhost:5000

<br>

### Para criação de um usuário: 
POST /users

exemplo de requisição:

```
{
    "nome": "Keila Passos",
    "cpf": "11111111111",
    "data_nascimento": "1995-05-11",
    "sexo": "F",
    "peso": "44.60",
    "altura": "1.56",
    "nacionalidade": "Brasileira"
}
```

*Observação: A requisição pode ser enviada sem informar o campo <b>nacionalidade</b>. Quando enviada sem este campo, por padrão esse campo é preenchido com o valor: <b>Brasileira</b>

<br>
*** A aplicação continua com outros endpoints, readme em andamento



