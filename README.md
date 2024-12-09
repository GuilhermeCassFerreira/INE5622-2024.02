# INE5622-2024.02

### Trabalho final da disciplina de Introdução a Compiladores

Analisador Léxico + Analisador Sintático implementados em Python.

[self link](https://github.com/GuilhermeCassFerreira/INE5622-2024.02)

---

## Instruções de execução do projeto

Pré-requisitos:

- [Python 3](https://www.python.org/downloads/);
- [PLY (Python Lex-Yacc)](https://www.dabeaz.com/ply/);

É necessário instalar estas dependências através do gerenciador de pacotes do seu sistema operacional antes de tentar executar o projeto.

Para instalar o PLY, você pode usar o pip:

```bash
pip install ply
```

---

Para executar o projeto, siga os passos abaixo:

1. **Clone o repositório** (se aplicável):

```bash
git clone https://github.com/GuilhermeCassFerreira/INE5622-2024.02.git
cd INE5622-2024.02
```

2. **Execute o script `run_parser.py`**:

```bash
python3 run_parser.py
```

O script exibirá uma lista de arquivos no diretório `~/INE5622-2024.02/test-sources` e permitirá que você selecione um deles para ser analisado pelo parser.

---

## Estrutura do Projeto

- `lexer_parte_b.py`: Implementação do analisador léxico (lexer) usando PLY.
- `parser.py`: Implementação do analisador sintático (parser) preditivo guiado por tabela.
- `run_parser.py`: Script principal para executar o parser em arquivos de entrada.
- `test-sources`: Diretório contendo arquivos de teste para o analisador.

---

## Explicação dos Arquivos

### `lexer_parte_b.py`

Este arquivo implementa o analisador léxico (lexer) usando a biblioteca PLY. O lexer é responsável por ler o código-fonte e dividir o texto em tokens, que são as unidades básicas de significado (como palavras-chave, identificadores, operadores, etc.).

#### Como Executar

Para testar o analisador léxico diretamente, você pode usar o comando:

```bash
python3 lexer_parte_b.py
```

### `parser.py`

Este arquivo implementa o analisador sintático (parser) preditivo guiado por tabela. O parser é responsável por analisar a sequência de tokens gerada pelo lexer e verificar se a estrutura do código-fonte está de acordo com a gramática definida. Ele também pode construir uma árvore de análise sintática.

#### Como Executar

Para testar o analisador sintático diretamente, você pode usar o comando:

```bash
python3 parser.py
```

### `run_parser.py`

Este é o script principal que integra o lexer e o parser. Ele permite que você selecione um arquivo de entrada a partir de uma lista de arquivos no diretório `test-sources` e executa o parser nesse arquivo. Isso elimina a necessidade de alterar manualmente o caminho do arquivo no `parser.py`.

#### Como Executar

Para executar o script principal e selecionar um arquivo de teste, use o comando:

```bash
python3 run_parser.py
```

O script exibirá uma lista de arquivos no diretório `~/INE5622-2024.02/test-sources` e permitirá que você selecione um deles para ser analisado pelo parser.

---

## Exemplos de Execução

### Executando o Analisador Léxico

Para testar o analisador léxico diretamente, você pode usar o script `lexer_parte_b.py`:

```bash
python3 lexer_parte_b.py
```

### Executando o Analisador Sintático

Para testar o analisador sintático diretamente, você pode usar o script `parser.py`:

```bash
python3 parser.py
```

### Executando o Script Principal

Para executar o script principal e selecionar um arquivo de teste, use o comando:

```bash
python3 run_parser.py
```

O script exibirá uma lista de arquivos no diretório `~/INE5622-2024.02/test-sources` e permitirá que você selecione um deles para ser analisado pelo parser.

---
---

## Integrantes do Grupo

- Bruno Vazquez Lafaiete (20102277)
- Guilherme Cassiano Ferreira Silva (23250871)
- Victor Luiz de Souza (21105576)

---