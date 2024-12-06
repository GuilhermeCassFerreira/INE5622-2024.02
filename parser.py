import os

import lexer_parte_b as lexer

M = {
    "S": {
        "$": ["MAIN", "$"],
        "def": ["MAIN", "$"],
        "id": ["MAIN", "$"],
        "{": ["MAIN", "$"],
        "int": ["MAIN", "$"],
        ";": ["MAIN", "$"],
        "print": ["MAIN", "$"],
        "return": ["MAIN", "$"],
        "if": ["MAIN", "$"],
    },
    "MAIN": {
        "$": [],
        "def": ["FLIST"],
        "id": ["STMT"],
        "{": ["STMT"],
        "int": ["STMT"],
        ";": ["STMT"],
        "print": ["STMT"],
        "return": ["STMT"],
        "if": ["STMT"],
    },
    "FLIST": {
        "def": ["FDEF", "FLIST'"],
    },
    "FLIST'": {
        "$": [],
        "def": ["FLIST"],
    },
    "FDEF": {
        "def": ["def", "id(", "PARLIST", ")", "{", "STMTLIST", "}"],
    },
    "PARLIST": {
        ")": [],
        "int": ["int", "id", "PARLIST'"],
    },
    "PARLIST'": {
        ")": [],
        ",": [",", "PARLIST"],
    },
    "VARLIST": {
        "id": ["id", "VARLIST'"],
    },
    "VARLIST'": {
        ",": [",", "VARLIST"],
        ";": [],
    },
    "STMT": {
        "id": ["ATRIBST", ";"],
        "{": ["{", "STMTLIST", "}"],
        "int": ["int", "VARLIST", ";"],
        ";": [";"],
        "print": ["PRINTST", ";"],
        "return": ["RETURNST", ";"],
        "if": ["IFSTMT"],
    },
    "ATRIBST": {
        "id": ["id", ":=", "ATRIBST'"],
    },
    "ATRIBST'": {
        "id(": ["FCALL"],
        "id": ["EXPR"],
        "(": ["EXPR"],
        "num": ["EXPR"],
    },
    "FCALL": {
        "id(": ["id(", "PARLISTCALL", ")"],
    },
    "PARLISTCALL": {
        ")": [],
        "id": ["id", "PARLISTCALL'"],
    },
    "PARLISTCALL'": {
        ")": [],
        ",": [",", "PARLISTCALL"],
    },
    "PRINTST": {
        "print": ["print", "EXPR"],
    },
    "RETURNST": {
        "return": ["return", "RETURNST'"],
    },
    "RETURNST'": {
        "id": ["id"],
        ";": [],
    },
    "IFSTMT": {
        "if": ["if", "(", "EXPR", ")", "STMT", "IFSTMT'"],
    },
    "IFSTMT'": {
        "else": ["else", "STMT"],
        "$": [],
        "def": [],
        "id": [],
        "}": [],
        "int": [],
        ";": [],
        "print": [],
        "return": [],
        "if": [],
    },
    "STMTLIST": {
        "id": ["STMT", "STMTLIST'"],
        "{": ["STMT", "STMTLIST'"],
        "int": ["STMT", "STMTLIST'"],
        ";": ["STMT", "STMTLIST'"],
        "print": ["STMT", "STMTLIST'"],
        "return": ["STMT", "STMTLIST'"],
        "if": ["STMT", "STMTLIST'"],
    },
    "STMTLIST'": {
        "id": ["STMT", "STMTLIST'"],
        "{": ["STMT", "STMTLIST'"],
        "int": ["STMT", "STMTLIST'"],
        ";": ["STMT", "STMTLIST'"],
        "print": ["STMT", "STMTLIST'"],
        "return": ["STMT", "STMTLIST'"],
        "if": ["STMT", "STMTLIST'"],
        "}": [],
    },
    "EXPR": {
        "id": ["NUMEXPR", "EXPR'"],
        "(": ["NUMEXPR", "EXPR'"],
        "num": ["NUMEXPR", "EXPR'"],
    },
    "EXPR'": {
        ")": [],
        ";": [],
        "<": ["<", "NUMEXPR"],
        "<=": ["<=", "NUMEXPR"],
        ">": [">", "NUMEXPR"],
        ">=": [">=", "NUMEXPR"],
        "==": ["==", "NUMEXPR"],
        "<>": ["<>", "NUMEXPR"],
    },
    "NUMEXPR": {
        "id": ["TERM", "NUMEXPR'"],
        "(": ["TERM", "NUMEXPR'"],
        "num": ["TERM", "NUMEXPR'"],
    },
    "NUMEXPR'": {
        ")": [],
        ";": [],
        "<": [],
        "<=": [],
        ">": [],
        ">=": [],
        "==": [],
        "<>": [],
        "+": ["+", "TERM", "NUMEXPR'"],
        "-": ["-", "TERM", "NUMEXPR'"],
    },
    "TERM": {
        "id": ["FACTOR", "TERM'"],
        "(": ["FACTOR", "TERM'"],
        "num": ["FACTOR", "TERM'"],
    },
    "TERM'": {#todo TA ERRADO AQUI FALTANDO COISA
        ")": [],
        ";": [],
        "+": [],
        "-": [],
        "*": ["*", "FACTOR", "TERM'"],
        "/": ["/", "FACTOR", "TERM'"],
    },
    "FACTOR": {
        "id": ["id"],
        "(": ["(", "NUMEXPR", ")"],
        "num": ["num"],
    },
}


# Algoritmo de Parsing
# current_token = a // top = X
def predictive_parser(tokens, table, start_symbol):
    tokens.append("$")
    stack = ["$", start_symbol]  # pilha começa com $ e o símbolo inicial
    productions_used = []  # armazena as producos usadas

    index = 0  # aponta pro prox símbolo no buffer de entrada
    current_token = tokens[0]  # primeiro símbolo de w
    top = stack[-1] # simbolo no topo da pilha

    while current_token != "$":
        if top == current_token:  # "Match"
            print(f"Match: {top}")
            stack.pop()
            index += 1
            current_token = tokens[index]
        elif top not in table:
            print(f"Error: Unexpected terminal '{top}'")  # terminal, mas não era o do input
            return False
        elif current_token not in table[top]: ##se a producao nao existe pro não terminal x terminal, nao tem como prosseguir
            print(f"Error: Unexpected token '{current_token}' for non-terminal '{top}'")
            return False
        elif table[top]:  # se está em table, é nao terminal
            production = table[top][current_token]
            print(f"Using production: {production}")
            productions_used.append(production)

            # deequeue e enqueue a produção
            stack.pop()

            if production:  # caso produza episilon não empilha
                stack.extend(reversed(production))  # empilha os simbolos da producao
        top = stack[-1] # atualiza X e repete


    print("Parsing completed successfully!")
    return True

if __name__ == "__main__":
    # filename = input("forneça o caminho para o arquivo com os tokens: ")
    filename = os.path.expanduser("./entrada_correta.lsi")
    filename = os.path.abspath(filename)
    if not os.path.isfile(filename):
        print(f"Arquivo '{filename}' não encontrado.")
    else:
        tokens = lexer.get_tokens(filename)
        print(tokens)
        result = predictive_parser(tokens, M, "S")
        if result:
            print("Success! Program belongs to the language.")
        else:
            print("Error! Program does not belong to the language.")

