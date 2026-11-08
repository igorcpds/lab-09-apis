from flask import Flask, jsonify, request

app = Flask(__name__)

# Base de dados simulada em memória para a API RESTful
livros = [
    {"id": 1, "titulo": "1984", "autor": "George Orwell"},
    {"id": 2, "titulo": "Código Limpo", "autor": "Robert C. Martin"}
]

@app.route("/", methods=["GET"])
def home():
    return jsonify({"mensagem": "Olá, Mundo! API Flask a funcionar com sucesso!"}), 200

@app.route("/api/livros", methods=["GET"])
def listar_livros():
    return jsonify(livros), 200

@app.route("/api/livros", methods=["POST"])
def adicionar_livro():
    novo_dado = request.get_json()
    if not novo_dado or "titulo" not in novo_dado or "autor" not in novo_dado:
        return jsonify({"erro": "Campos 'titulo' e 'autor' são obrigatórios"}), 400

    novo_livro = {
        "id": len(livros) + 1,
        "titulo": novo_dado.get("titulo"),
        "autor": novo_dado.get("autor")
    }
    livros.append(novo_livro)
    return jsonify(novo_livro), 201

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=True)
