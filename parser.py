# Exemplo de tabela de análise sintática (simplificada para referência)
M = {
    "S": {
        "MAIN": "S → MAIN $",
    },
    "MAIN": {
        "$": "MAIN → ε",
        "def": "MAIN → FLIST",
        "id": "MAIN → STMT",
    },
    "FLIST": {
        "def": "FLIST → FDEF FLIST'",
    },
    "FLIST'": {
        "$": "FLIST' → ε",
        "def": "FLIST' → FLIST",
    },
    "FDEF": {
        "def": "FDEF → def id ( PARLIST ) { STMTLIST }",
    },
    "PARLIST": {
        "int": "PARLIST → int id PARLIST'",
        "$": "PARLIST → ε",
    },
    "PARLIST'": {
        ",": "PARLIST' → , PARLIST",
        "$": "PARLIST' → ε",
    },
    "STMT": {
        "id": "STMT → ATRIBST ;",
        "{": "STMT → { STMTLIST }",
        "int": "STMT → int VARLIST ;",
        ";": "STMT → ;",
        "print": "STMT → PRINTST ;",
        "return": "STMT → RETURNST ;",
        "if": "STMT → IFSTMT",
    },
    "ATRIBST": {
        "id": "ATRIBST → id := ATRIBST'",
    },
    "ATRIBST'": {
        "id": "ATRIBST' → id AATRIBST'",
        "(": "ATRIBST' → ( NUMEXPR ) TERM' NUMEXPR' EXPR'",
        "num": "ATRIBST' → num TERM' NUMEXPR' EXPR'",
    },
    "AATRIBST'": {
        "(": "AATRIBST' → ( PARLISTCALL )",
        "$": "AATRIBST' → ε",
    },
    "FCALL": {
        "id": "FCALL → id ( PARLISTCALL )",
    },
    "PARLISTCALL": {
        "id": "PARLISTCALL → id PARLISTCALL'",
        "$": "PARLISTCALL → ε",
    },
    "PARLISTCALL'": {
        ",": "PARLISTCALL' → , PARLISTCALL",
        "$": "PARLISTCALL' → ε",
    },
    "PRINTST": {
        "print": "PRINTST → print EXPR",
    },
    "RETURNST": {
        "return": "RETURNST → return RETURNST'",
    },
    "RETURNST'": {
        "id": "RETURNST' → id",
        "$": "RETURNST' → ε",
    },
    "IFSTMT": {
        "if": "IFSTMT → if ( EXPR ) STMT IFSTMT''",
    },
    "IFSTMT'": {
        "else": "IFSTMT' → else STMT",
        "$": "IFSTMT' → ε",
    },
    "STMTLIST": {
        "id": "STMTLIST → STMT STMTLIST'",
        "{": "STMTLIST → STMT STMTLIST'",
        "int": "STMTLIST → STMT STMTLIST'",
        ";": "STMTLIST → STMT STMTLIST'",
        "print": "STMTLIST → STMT STMTLIST'",
        "return": "STMTLIST → STMT STMTLIST'",
        "if": "STMTLIST → STMT STMTLIST'",
    },
    "STMTLIST'": {
        "$": "STMTLIST' → ε",
        "id": "STMTLIST' → STMT STMTLIST'",
        "{": "STMTLIST' → STMT STMTLIST'",
        "int": "STMTLIST' → STMT STMTLIST'",
        ";": "STMTLIST' → STMT STMTLIST'",
        "print": "STMTLIST' → STMT STMTLIST'",
        "return": "STMTLIST' → STMT STMTLIST'",
        "if": "STMTLIST' → STMT STMTLIST'",
    },
    "EXPR": {
        "id": "EXPR → NUMEXPR EXPR'",
        "num": "EXPR → NUMEXPR EXPR'",
    },
    "EXPR'": {
        "$": "EXPR' → ε",
        "<": "EXPR' → < NUMEXPR",
        "<=": "EXPR' → <= NUMEXPR",
        ">": "EXPR' → > NUMEXPR",
        ">=": "EXPR' → >= NUMEXPR",
        "==": "EXPR' → == NUMEXPR",
        "<>": "EXPR' → <> NUMEXPR",
    },
    "NUMEXPR": {
        "id": "NUMEXPR → TERM NUMEXPR'",
        "num": "NUMEXPR → TERM NUMEXPR'",
    },
    "NUMEXPR'": {
        "$": "NUMEXPR' → ε",
        "+": "NUMEXPR' → + TERM NUMEXPR'",
        "-": "NUMEXPR' → - TERM NUMEXPR'",
    },
    "TERM": {
        "id": "TERM → FACTOR TERM'",
        "num": "TERM → FACTOR TERM'",
    },
    "TERM'": {
        "$": "TERM' → ε",
        "*": "TERM' → * FACTOR TERM'",
        "/": "TERM' → / FACTOR TERM'",
    },
    "FACTOR": {
        "id": "FACTOR → id",
        "num": "FACTOR → num",
        "(": "FACTOR → ( NUMEXPR )",
    },
}


# Algoritmo de Parsing
# current_token = a // top = X
def predictive_parser(tokens, table, start_symbol):
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
        elif not table[top][current_token]: ## se a produção não existe para aquele não terminal x terminal, não tem como prosseguir
            print(f"Error: Unexpected token '{current_token}' for non-terminal '{top}'")
            return False
        elif table[top][current_token]:  # se está em table, é Não-terminal
            production = table[top][current_token]
            print(f"Using production: {production}")
            productions_used.append(production)

            # Desempilha e empilha a produção
            stack.pop()

            _, rhs = production.split("→")
            symbols = rhs.strip().split()
            if symbols != ["ε"]:  # caso produza episilon não empilha
                stack.extend(reversed(symbols))  # Empilha os símbolos da produção
        top = stack[-1] ## Atualiza X e repete


    print("Parsing completed successfully!")
    return True

    # return True if index == len(tokens) else False

# Exemplo de tokens de entrada
tokens = [
    "MAIN", "def", "id", "(", "int", "id", ")", "{", "id", ":=", "num", ";", "def", "id", "(", "int", "id", ")", "{", "id", ":=", "num", ";", "}", "}", "$"
]
# Executa o analisador
result = predictive_parser(tokens, M, "S")
if result:
    print("Success! Program belongs to the language.")
else:
    print("Error! Program does not belong to the language.")