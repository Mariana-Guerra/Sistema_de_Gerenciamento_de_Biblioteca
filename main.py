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

        # FUNÇÕES PRINCIPAIS

def cadastrar_livro():
    """Cadastra um novo livro e retorna True se conseguiu"""
    titulo = input("Título: ").strip()
    autor = input("Autor: ").strip()
    ano = input("Ano de publicação: ").strip()
    isbn = input("ISBN: ").strip()

    # Verifica duplicidade pelo ISBN
    for livro in livros:
        if livro["isbn"] == isbn:
            print("\nErro: Este livro já está cadastrado!\n")
            return False

    novo_livro = {
        "titulo": titulo,
        "autor": autor,
        "ano": ano,
        "isbn": isbn,
        "status": "Disponível"
    }
    livros.append(novo_livro)
    salvar_livros()
    print("\nLivro cadastrado com sucesso!\n")
    return True

def emprestar_livro():
    """Registra empréstimo de um livro"""
    titulo = input("Digite o título do livro para emprestar: ").strip()
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["status"] == "Disponível":
                livro["status"] = "Emprestado"
                salvar_livros()
                print("Livro emprestado com sucesso!")
                return True
            else:
                print("Este livro já está emprestado.")
                return False
    print("Livro não encontrado.")
    return False

def devolver_livro():
    """Registra devolução de um livro"""
    titulo = input("Digite o título do livro para devolver: ").strip()
    for livro in livros:
        if livro["titulo"].lower() == titulo.lower():
            if livro["status"] == "Emprestado":
                livro["status"] = "Disponível"
                salvar_livros()
                print("Livro devolvido com sucesso!")
                return True
            else:
                print("Este livro já está disponível.")
                return False
    print("Livro não encontrado.")
    return False

def listar_livros():
    """Lista todos os livros cadastrados"""
    if not livros:
        print("\nNenhum livro cadastrado.\n")
        return

    print("\n===== ACERVO DA BIBLIOTECA =====")
    for livro in livros:
        print(f"Título: {livro['titulo']}")
        print(f"Autor: {livro['autor']}")
        print(f"Ano: {livro['ano']}")
        print(f"ISBN: {livro['isbn']}")
        print(f"Status: {livro['status']}")
        print("-" * 30)

def buscar_livro():
    """Busca livro por título ou autor"""
    termo = input("Digite título ou autor para buscar: ").strip().lower()
    resultados = [l for l in livros if termo in l["titulo"].lower() or termo in l["autor"].lower()]

    if not resultados:
        print("Nenhum livro encontrado.")
        return []

    print(f"\n{len(resultados)} livro(s) encontrado(s):")
    for livro in resultados:
        print(f"- {livro['titulo']} | {livro['autor']} | {livro['status']}")
    return resultados