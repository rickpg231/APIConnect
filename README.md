# APIConnect

API REST desenvolvida em Python utilizando Flask, com o objetivo de demonstrar a criação e o consumo de uma API seguindo os princípios básicos de uma arquitetura cliente-servidor.

O projeto implementa operações CRUD (Create, Read, Update e Delete) para gerenciamento de usuários.

## Tecnologias utilizadas

* Python 3
* Flask
* JSON
* HTTP/REST
* Git e GitHub

## Objetivo do projeto

O APIConnect foi desenvolvido como um projeto prático para aplicação dos conceitos de desenvolvimento de APIs REST, incluindo:

* Criação de endpoints;
* Recebimento e envio de dados em JSON;
* Métodos HTTP;
* Códigos de status HTTP;
* Operações CRUD;
* Validação básica de dados;
* Tratamento de erros;
* Versionamento do código utilizando Git.

## Estrutura do projeto

```text
APIConnect/
├── .gitignore
├── README.md
└── app.py
```

### app.py

Arquivo principal da aplicação. Contém a configuração do Flask e os endpoints responsáveis pelo gerenciamento dos usuários.

### .gitignore

Define os arquivos e diretórios que não devem ser enviados para o controle de versão do Git.

### README.md

Documento com informações sobre o projeto, instalação, execução e utilização da API.

## Instalação

### 1. Clonar o repositório

```bash
git clone https://github.com/rickpg231/APIConnect.git
```

### 2. Acessar a pasta do projeto

```bash
cd APIConnect
```

### 3. Criar um ambiente virtual

No Windows:

```bash
python -m venv venv
```

### 4. Ativar o ambiente virtual

```bash
venv\Scripts\activate
```

### 5. Instalar o Flask

```bash
pip install flask
```

## Executando a aplicação

Com o ambiente virtual ativado, execute:

```bash
python app.py
```

A API será disponibilizada localmente em:

```text
http://127.0.0.1:5000
```

ou:

```text
http://localhost:5000
```

## Endpoints

A API possui os seguintes endpoints:

| Método | Endpoint               | Descrição                |
| ------ | ---------------------- | ------------------------ |
| GET    | `/users`               | Lista todos os usuários  |
| GET    | `/users/<int:user_id>` | Busca um usuário pelo ID |
| POST   | `/users`               | Cadastra um novo usuário |
| PUT    | `/users/<int:user_id>` | Atualiza um usuário      |
| DELETE | `/users/<int:user_id>` | Exclui um usuário        |

## Exemplos de utilização

### GET - Listar usuários

Requisição:

```http
GET /users
```

Resposta:

```json
{
    "data": [
        {
            "id": 1,
            "nome": "Ricardo",
            "email": "ricardo@email.com"
        }
    ]
}
```

### GET - Buscar usuário por ID

Requisição:

```http
GET /users/1
```

Resposta:

```json
{
    "data": {
        "id": 1,
        "nome": "Ricardo",
        "email": "ricardo@email.com"
    }
}
```

Caso o usuário não seja encontrado:

```json
{
    "error": "Usuário não encontrado."
}
```

Status HTTP:

```text
404 Not Found
```

### POST - Cadastrar usuário

Requisição:

```http
POST /users
```

Header:

```text
Content-Type: application/json
```

Body:

```json
{
    "nome": "Ricardo",
    "email": "ricardo@email.com"
}
```

Resposta:

```json
{
    "data": {
        "id": 1,
        "nome": "Ricardo",
        "email": "ricardo@email.com"
    }
}
```

Status HTTP:

```text
201 Created
```

Os campos `nome` e `email` são obrigatórios.

### PUT - Atualizar usuário

Requisição:

```http
PUT /users/1
```

Header:

```text
Content-Type: application/json
```

Body:

```json
{
    "nome": "Ricardo Borges",
    "email": "ricardoborges@email.com"
}
```

Resposta:

```json
{
    "data": {
        "id": 1,
        "nome": "Ricardo Borges",
        "email": "ricardoborges@email.com"
    }
}
```

Status HTTP:

```text
200 OK
```

### DELETE - Excluir usuário

Requisição:

```http
DELETE /users/1
```

Resposta:

```json
{
    "data": "Usuário removido com sucesso."
}
```

Status HTTP:

```text
200 OK
```

## Validações e tratamento de erros

A API possui validações básicas para garantir que as requisições estejam no formato esperado.

### JSON inválido

Caso o corpo da requisição não contenha um JSON válido:

```json
{
    "error": "JSON inválido."
}
```

Status:

```text
400 Bad Request
```

### Campos obrigatórios

Nas operações de criação e atualização, os campos `nome` e `email` são obrigatórios.

Resposta:

```json
{
    "error": "Os campos nome e email são obrigatórios."
}
```

Status:

```text
400 Bad Request
```

### Usuário não encontrado

Quando é solicitado um usuário que não existe:

```json
{
    "error": "Usuário não encontrado."
}
```

Status:

```text
404 Not Found
```

## Armazenamento dos dados

Atualmente, o projeto utiliza uma estrutura de dados em memória para armazenar os usuários.

Isso significa que os dados são mantidos apenas enquanto a aplicação estiver em execução. Ao reiniciar o servidor, os usuários cadastrados são perdidos.

Essa abordagem foi utilizada para simplificar a implementação inicial da API.

## Testando a API

A API pode ser testada utilizando ferramentas como:

* Postman;
* Insomnia;
* Thunder Client;
* cURL.

Exemplo utilizando cURL:

```bash
curl http://127.0.0.1:5000/users
```

Para cadastrar um usuário:

```bash
curl -X POST http://127.0.0.1:5000/users ^
-H "Content-Type: application/json" ^
-d "{\"nome\":\"Ricardo\",\"email\":\"ricardo@email.com\"}"
```

## Status do projeto

Em desenvolvimento.

### Próximas melhorias

Algumas melhorias que podem ser implementadas futuramente:

* Implementação de banco de dados;
* Integração com SQLite, PostgreSQL ou MySQL;
* Validação mais completa dos dados;
* Autenticação e autorização;
* Documentação utilizando Swagger/OpenAPI;
* Testes automatizados;
* Separação da aplicação em diferentes módulos;
* Configuração de variáveis de ambiente;
* Deploy da API em um servidor.

## Versionamento

O projeto utiliza Git para controle de versão e GitHub para hospedagem do código-fonte.

Repositório:

https://github.com/rickpg231/APIConnect.git

## Autor

**Ricardo Borges**

Projeto desenvolvido para fins acadêmicos e de aprendizado em desenvolvimento de APIs REST com Python e Flask.
