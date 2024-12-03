# Bruno Vazquez Lafaiete (20102277), Guilherme Cassiano Ferreira Silva (23250871), Victor Luiz de Souza (21105576)

import ply.lex as lex
import sys
import os

# Lista de tokens
tokens = [
    'ID', 'NUM', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
    'LT', 'GT', 'LE', 'GE', 'EQ', 'NE', 'LPAREN', 'RPAREN',
    'LBRACE', 'RBRACE', 'SEMI', 'COMMA', 'DEF', 'IF', 'ELSE',
    'PRINT', 'RETURN', 'INT'
]

# Regras regulares para tokens simples
t_PLUS    = r'\+'
t_MINUS   = r'-'
t_TIMES   = r'\*'
t_DIVIDE  = r'/'
t_ASSIGN  = r':='
t_LT      = r'<'
t_GT      = r'>'
t_LE      = r'<='
t_GE      = r'>='
t_EQ      = r'=='
t_NE      = r'<>'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LBRACE  = r'\{'
t_RBRACE  = r'\}'
t_SEMI    = r';'
t_COMMA   = r','

reserved = {
    'def': 'DEF',
    'if': 'IF',
    'else': 'ELSE',
    'print': 'PRINT',
    'return': 'RETURN',
    'int': 'INT',
}
# Regras para palavras-chave
def t_DEF(t):
    r'def'
    return t

def t_IF(t):
    r'if'
    return t

def t_ELSE(t):
    r'else'
    return t

def t_PRINT(t):
    r'print'
    return t

def t_RETURN(t):
    r'return'
    return t

def t_INT(t):
    r'int'
    return t

# Regra para identificadores (variáveis e funções)
def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value, 'ID')
    return t

# Regra para constantes numéricas
def t_NUM(t):
    r'\d+'
    t.value = int(t.value)  # Converte o valor para inteiro
    return t

# Ignorar espaços em branco e quebras de linha
t_ignore = ' \t'

# Ignorar comentários
def t_COMMENT(t):
    r'\#.*'
    pass

# Regra para lidar com novas linhas e atualizar o número de linha
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Tratamento de erros
def t_error(t):
    print(f"Erro léxico: Caractere inválido '{t.value[0]}' na linha {t.lineno}, coluna {t.lexpos}")
    t.lexer.skip(1)

# Criação do lexer
lexer = lex.lex()

# Função para ler e testar o lexer com um arquivo de entrada
def test_lexer(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
    lexer.input(input_data)
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

def get_tokens(file_path):
    with open(file_path, 'r') as file:
        input_data = file.read()
    lexer.input(input_data)
    tokens_list = []
    while True:
        tok = lexer.token()
        if not tok:
            break
        if tok.type == 'ID' or tok.type =='NUM':  # Verifica se o token é do tipo ID TODO melhorar esse if else para tratar no lexer antes
            tokens_list.append(str(tok.type).lower())  # Adiciona 'id' como tipo padrão
        else:
            tokens_list.append(tok.value)  # Adiciona o valor do token diretamente
    return tokens_list

if __name__ == "__main__":
    # filename = input("Forneça o caminho para o arquivo com os tokens: ")
    filename = "entrada_correta.lsi"
    filename = os.path.expanduser(filename)
    filename = os.path.abspath(filename)
    if not os.path.isfile(filename):
        print(f"Arquivo '{filename}' não encontrado.")
    else:
        print(get_tokens(filename))

