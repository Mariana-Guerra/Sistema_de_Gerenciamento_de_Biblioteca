# Sistema_de_Gerenciamento_de_Biblioteca

O **Sistema de Gerenciamento de Biblioteca** é um programa desenvolvido em Python para controlar o acervo de uma biblioteca.
O sistema permite cadastrar livros, registrar empréstimos e devoluções, listar os livros cadastrados, realizar buscas por título ou autor e ordenar o acervo por título, autor ou ano de publicação.
Os dados dos livros são armazenados em um arquivo `livros.csv`, permitindo que o catálogo seja mantido mesmo depois que o programa é encerrado.

## Como executar o programa
1. Baixe ou clone este repositório.
2. Abra o terminal na pasta do projeto.
3. Execute o arquivo principal com:
```bash
python main.py
```
No Windows, também pode ser necessário utilizar:
```bash
py main.py
```
O sistema abrirá o menu principal no terminal.
O arquivo `livros.csv` é utilizado para armazenar os livros. Caso ele ainda não exista, será criado automaticamente quando um livro for cadastrado.

## Principais funcionalidades

 **Cadastrar livro**
- Permite informar título, autor, ano de publicação e ISBN.
- O sistema verifica se o ISBN já está cadastrado.
- Novos livros são cadastrados inicialmente com o status **Disponível**.

 **Emprestar livro**
- Busca um livro pelo título.
- Altera o status de **Disponível** para **Emprestado**.
- Impede o empréstimo de um livro que já esteja emprestado.

 **Devolver livro**
- Busca um livro pelo título.
- Altera o status de **Emprestado** para **Disponível**.
- Informa caso o livro já esteja disponível.

 **Listar livros**
- Exibe todos os livros cadastrados.
- Mostra título, autor, ano, ISBN e status.

 **Buscar livro**
- Permite pesquisar por título ou autor.
- A busca não diferencia letras maiúsculas e minúsculas.
- Também permite encontrar resultados utilizando apenas parte do título ou nome do autor.

 **Ordenar livros**
Permite ordenar o acervo por:
- Título
- Autor
- Ano de publicação
- A ordenação é feita utilizando o método da bolha (*Bubble Sort*).

 **Persistência dos dados**
- Os livros são salvos no arquivo `livros.csv`.
- Os dados são carregados automaticamente quando o programa é iniciado.

## Requisitos técnicos aplicados

### 1. Menu principal com `if/elif/else`
O menu principal está implementado na função `menu()`.
O programa apresenta as opções de cadastrar, emprestar, devolver, listar, buscar, ordenar e sair. As escolhas do usuário são tratadas utilizando `if`, `elif` e `else`.

### 2. Estrutura de repetição `while`
Na função `menu()`, um `while True` mantém o menu funcionando continuamente.
O programa só encerra quando o usuário escolhe a opção `0 - Sair`, utilizando `break`.

### 3. Funções próprias
O projeto foi dividido em várias funções para organizar melhor o código:
`carregar_livros()`
`salvar_livros()`
`cadastrar_livro()`
`emprestar_livro()`
`devolver_livro()`
`listar_livros()`
`buscar_livro()`
`ordenar_livros()`
`menu()`

### 4. Lista de livros em memória
Os livros são armazenados na variável `livros`, que é uma lista de dicionários.
Cada dicionário representa um livro e possui os campos:
`titulo`
`autor`
`ano`
`isbn`
`status`

### 5. Persistência em arquivo
A persistência é realizada utilizando o arquivo `livros.csv`.
As funções responsáveis por isso são:
`carregar_livros()` — lê os dados do arquivo quando o programa inicia.
`salvar_livros()` — grava os dados da lista no arquivo após alterações.
Para trabalhar com o CSV são utilizadas as bibliotecas padrão `csv` e `os`.

### 6. Biblioteca padrão do Python
O projeto não utiliza pacotes externos.
Foram utilizadas apenas bibliotecas que fazem parte da instalação padrão do Python:
```python
import csv
import os
```

### 7. Organização e comentários
O código foi separado em partes de acordo com sua responsabilidade, como:
- Funções de persistência
- Funções principais
- Menu principal
Também foram adicionados comentários e *docstrings* para explicar as partes importantes da lógica.

## Estrutura do projeto
```text
sistema-biblioteca/
│
├── main.py
├── livros.csv
└── README.md
```

## Tecnologias utilizadas

 **Python 3**
 **CSV**
 **Git/GitHub**
 Bibliotecas padrão `csv` e `os`

## Autor
Projeto desenvolvido por Mariana Guerra como atividade acadêmica de programação em Python.
