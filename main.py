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

def ordenar_livros():
    """Ordena a listagem de livros"""
    print("\nOrdenar por:")
    print("1 - Título")
    print("2 - Autor")
    print("3 - Ano")
    op = input("Escolha: ")

    if op == "1":
        # Ordenar por Título - método da bolha
        for i in range(len(livros)):
            for j in range(0, len(livros) - i - 1):
                if livros[j]["titulo"] > livros[j + 1]["titulo"]:
                    livros[j], livros[j + 1] = livros[j + 1], livros[j]

    elif op == "2":
        # Ordenar por Autor
        for i in range(len(livros)):
            for j in range(0, len(livros) - i - 1):
                if livros[j]["autor"] > livros[j + 1]["autor"]:
                    livros[j], livros[j + 1] = livros[j + 1], livros[j]

    elif op == "3":
        # Ordenar por Ano
        for i in range(len(livros)):
            for j in range(0, len(livros) - i - 1):
                if livros[j]["ano"] > livros[j + 1]["ano"]:
                    livros[j], livros[j + 1] = livros[j + 1], livros[j]
    else:
        print("Opção inválida.")
        return

    salvar_livros() # salva a nova ordem
    print("Livros ordenados!")
    listar_livros()

    # MENU PRINCIPAL

def menu():
    """Controla o fluxo do programa"""
    carregar_livros()

    while True:
        print("\n===== SISTEMA DE GERENCIAMENTO DE BIBLIOTECA =====")
        print("1 - Cadastrar livro")
        print("2 - Emprestar livro")
        print("3 - Devolver livro")
        print("4 - Listar livros")
        print("5 - Buscar livro")
        print("6 - Ordenar livros")
        print("0 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1": cadastrar_livro()
        elif opcao == "2": emprestar_livro()
        elif opcao == "3": devolver_livro()
        elif opcao == "4": listar_livros()
        elif opcao == "5": buscar_livro()
        elif opcao == "6": ordenar_livros()
        elif opcao == "0":
            print("\nEncerrando sistema. Até logo!")
            break
        else:
            print("Opção inválida! Tente novamente.")

if __name__ == "__main__":
    menu()