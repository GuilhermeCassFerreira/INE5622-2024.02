import os

import lexer_parte_b as lexer

# Exemplo de tabela de análise sintática (simplificada para referência)
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
        "def": ["def", "id", "(", "PARLIST", ")", "{", "STMTLIST", "}"],
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
        "id": ["id", "AATRIBST'"],
        "(": ["(", "NUMEXPR", ")", "TERM'", "NUMEXPR'", "EXPR'"],
        "num": ["num", "TERM'", "NUMEXPR'", "EXPR'"],
    },
    "AATRIBST'": {
        "(": ["(", "PARLISTCALL", ")"],
        "+": ["TERM'", "NUMEXPR'", "EXPR'"],
        "-": ["TERM'", "NUMEXPR'", "EXPR'"],
        "*": ["TERM'", "NUMEXPR'", "EXPR'"],
        "/": ["TERM'", "NUMEXPR'", "EXPR'"],
        "<": ["TERM'", "NUMEXPR'", "EXPR'"],
        "<=": ["TERM'", "NUMEXPR'", "EXPR'"],
        ">": ["TERM'", "NUMEXPR'", "EXPR'"],
        ">=": ["TERM'", "NUMEXPR'", "EXPR'"],
        "==": ["TERM'", "NUMEXPR'", "EXPR'"],
        "<>": ["TERM'", "NUMEXPR'", "EXPR'"],
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
        "if": ["if", "(", "EXPR", ")", "STMT", "IFSTMT''"],
    },
    "IFSTMT'": {
        "else": ["else", "STMT"],
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
        "+": ["+", "TERM", "NUMEXPR'"],
        "-": ["-", "TERM", "NUMEXPR'"],
    },
    "TERM": {
        "id": ["FACTOR", "TERM'"],
        "(": ["FACTOR", "TERM'"],
        "num": ["FACTOR", "TERM'"],
    },
    "TERM'": {
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
    stack = ["$", start_symbol]  # Pilha começa com $ e o símbolo inicial
    productions_used = []  # Armazena as produções usadas

    index = 0  # Aponta para o próximo símbolo no buffer de entrada
    current_token = tokens[0]  ## primeiro símbolo de w
    top = stack[-1] ## símbolo no topo da pilha

    while current_token != "$":
        if top == current_token:  # "Match"
            print(f"Match: {top}")
            stack.pop()
            index += 1
            current_token = tokens[index]
        elif top not in table:
            print(f"Error: Unexpected terminal '{top}'")  # Era terminal, mas não era o do input
            return False
        elif current_token not in table[top]: ## se a produção não existe para aquele não terminal x terminal, não tem como prosseguir
            print(f"Error: Unexpected token '{current_token}' for non-terminal '{top}'")
            return False
        elif table[top]:  # se está em table, é Não-terminal
            production = table[top][current_token]
            print(f"Using production: {production}")
            productions_used.append(production)

            # Desempilha e empilha a produção
            stack.pop()

            if production:  # caso produza episilon não empilha
                stack.extend(reversed(production))  # Empilha os símbolos da produção
        top = stack[-1] ## Atualiza X e repete


    print("Parsing completed successfully!")
    return True

    # return True if index == len(tokens) else False

# Executa o analisador
if __name__ == "__main__":
    # filename = input("Forneça o caminho para o arquivo com os tokens: ")
    filename = os.path.expanduser("./entrada_correta.lsi")
    filename = os.path.abspath(filename)
    if not os.path.isfile(filename):
        print(f"Arquivo '{filename}' não encontrado.")
    else:
        result = predictive_parser(lexer.get_tokens(filename), M, "S")
        if result:
            print("Success! Program belongs to the language.")
        else:
            print("Error! Program does not belong to the language.")

