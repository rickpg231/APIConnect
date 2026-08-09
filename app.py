from flask import Flask, request, jsonify

app = Flask(__name__)

# Simulação de banco de dados em memória
users = []
next_id = 1


# GET - Listar todos os usuários
@app.route('/users', methods=['GET'])
def get_users():
    return jsonify({"data": users}), 200


# GET - Buscar usuário por ID
@app.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return jsonify({"data": user}), 200

    return jsonify({"error": "Usuário não encontrado."}), 404


# POST - Cadastrar usuário
@app.route('/users', methods=['POST'])
def create_user():
    global next_id

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido."}), 400

    if "nome" not in data or "email" not in data:
        return jsonify({
            "error": "Os campos nome e email são obrigatórios."
        }), 400

    user = {
        "id": next_id,
        "nome": data["nome"],
        "email": data["email"]
    }

    users.append(user)

    next_id += 1

    return jsonify({"data": user}), 201


# PUT - Atualizar usuário
@app.route('/users/<int:user_id>', methods=['PUT'])
def update_user(user_id):

    data = request.get_json()

    if not data:
        return jsonify({"error": "JSON inválido."}), 400

    if "nome" not in data or "email" not in data:
        return jsonify({
            "error": "Os campos nome e email são obrigatórios."
        }), 400

    for user in users:
        if user["id"] == user_id:
            user["nome"] = data["nome"]
            user["email"] = data["email"]

            return jsonify({"data": user}), 200

    return jsonify({"error": "Usuário não encontrado."}), 404


# DELETE - Excluir usuário
@app.route('/users/<int:user_id>', methods=['DELETE'])
def delete_user(user_id):

    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return jsonify({
                "data": "Usuário removido com sucesso."
            }), 200

    return jsonify({"error": "Usuário não encontrado."}), 404


if __name__ == "__main__":
    app.run(debug=True)
