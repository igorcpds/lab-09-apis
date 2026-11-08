from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Livraria API - FastAPI", version="1.0")

class Livro(BaseModel):
    titulo: str
    autor: str

# Base de dados simulada em memória
catalogo = [
    {"id": 1, "titulo": "1984", "autor": "George Orwell"},
    {"id": 2, "titulo": "O Hobbit", "autor": "J.R.R. Tolkien"}
]

@app.get("/", status_code=200)
def home():
    return {"mensagem": "Olá, Mundo! API FastAPI a funcionar com sucesso!"}

@app.get("/api/livros", status_code=200)
def listar_livros():
    return catalogo

@app.post("/api/livros", status_code=201)
def criar_livro(livro: Livro):
    novo_livro = {
        "id": len(catalogo) + 1,
        "titulo": livro.titulo,
        "autor": livro.autor
    }
    catalogo.append(novo_livro)
    return novo_livro
