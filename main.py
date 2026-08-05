import csv
import os

ARQUIVO = "livros.csv"
CAMPOS = ["titulo", "autor", "ano", "isbn", "status"]
livros = []

# FUNÇÕES DE PERSISTÊNCIA

def carregar_livros():
    """Carrega os livros do arquivo CSV ao iniciar o programa"""
    global livros
    livros = []
    if os.path.exists(ARQUIVO):
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            leitor = csv.DictReader(f)
            for linha in leitor:
                livros.append(linha)

def salvar_livros():
    """Salva a lista de livros no arquivo CSV"""
    with open(ARQUIVO, "w", encoding="utf-8", newline="") as f:
        escritor = csv.DictWriter(f, fieldnames=CAMPOS)
        escritor.writeheader()
        escritor.writerows(livros)

        