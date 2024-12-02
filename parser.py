# Exemplo de tabela de análise sintática (simplificada para referência)
M = {
    # Inicial
    "S": {
        "T_FUNCDEF": "S → funcdef S",
        "$": "S → ε",
    },
    # Função
    "funcdef": {
        "T_FUNCDEF": "funcdef → T_FUNCDEF T_IDENT T_OPEN_PAREN parlist T_CLOSE_PAREN T_OPEN_BRACE stmtlist T_CLOSE_BRACE",
    },
    # Parâmetros
    "parlist": {
        "T_INT": "parlist → T_INT T_IDENT parlist_tail",
        "T_CLOSE_PAREN": "parlist → ε",
    },
    "parlist_tail": {
        "T_COMMA": "parlist_tail → T_COMMA T_INT T_IDENT parlist_tail",
        "T_CLOSE_PAREN": "parlist_tail → ε",
    },
    # Declarações
    "stmtlist": {
        "T_INT": "stmtlist → stmt stmtlist",
        "T_RETURN": "stmtlist → stmt stmtlist",
        "T_IDENT": "stmtlist → stmt stmtlist",
        "T_PRINT": "stmtlist → stmt stmtlist",
        "T_CLOSE_BRACE": "stmtlist → ε",
    },
    "stmt": {
        "T_INT": "stmt → T_INT T_IDENT T_SEMICOLON",
        "T_IDENT": "stmt → T_IDENT T_EQUALS_SIGN expr T_SEMICOLON",
        "T_PRINT": "stmt → T_PRINT expr T_SEMICOLON",
        "T_RETURN": "stmt → T_RETURN expr T_SEMICOLON",
    },
    # Expressões
    "expr": {
        "T_IDENT": "expr → T_IDENT expr_tail",
        "INT_LITERAL": "expr → term expr_tail",
    },
    "expr_tail": {
        "T_PLUS_SIGN": "expr_tail → T_PLUS_SIGN term expr_tail",
        "T_MINUS_SIGN": "expr_tail → T_MINUS_SIGN term expr_tail",
        "T_SEMICOLON": "expr_tail → ε",
    },
    # Termos e fatores
    "term": {
        "T_IDENT": "term → factor term_tail",
        "INT_LITERAL": "term → factor term_tail",
    },
    "term_tail": {
        "T_ASTERISK_SIGN": "term_tail → T_ASTERISK_SIGN factor term_tail",
        "T_SLASH_SIGN": "term_tail → T_SLASH_SIGN factor term_tail",
        "T_PLUS_SIGN": "term_tail → ε",
        "T_MINUS_SIGN": "term_tail → ε",
        "T_SEMICOLON": "term_tail → ε",
    },
    "factor": {
        "T_IDENT": "factor → T_IDENT",
        "INT_LITERAL": "factor → INT_LITERAL",
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
    "T_FUNCDEF", "T_IDENT", "T_OPEN_PAREN", "T_INT", "T_IDENT", "T_COMMA", "T_INT", "T_IDENT", "T_CLOSE_PAREN",
    "T_OPEN_BRACE", "T_INT", "T_IDENT", "T_COMMA", "T_IDENT", "T_SEMICOLON",
    "T_IDENT", "T_EQUALS_SIGN", "T_IDENT", "T_PLUS_SIGN", "T_IDENT", "T_SEMICOLON",
    "T_IDENT", "T_EQUALS_SIGN", "T_IDENT", "T_PLUS_SIGN", "T_IDENT", "T_ASTERISK_SIGN", "T_IDENT", "T_SEMICOLON",
    "T_RETURN", "T_IDENT", "T_SEMICOLON", "T_CLOSE_BRACE",
    "T_FUNCDEF", "T_IDENT", "T_OPEN_PAREN", "T_CLOSE_PAREN",
    "T_OPEN_BRACE", "T_INT", "T_IDENT", "T_COMMA", "T_IDENT", "T_COMMA", "T_IDENT", "T_SEMICOLON",
    "T_IDENT", "T_EQUALS_SIGN", "INT_LITERAL", "T_SEMICOLON",
    "T_IDENT", "T_EQUALS_SIGN", "INT_LITERAL", "T_SEMICOLON",
    "T_IDENT", "T_EQUALS_SIGN", "T_IDENT", "T_OPEN_PAREN", "T_IDENT", "T_COMMA", "T_IDENT", "T_CLOSE_PAREN", "T_SEMICOLON",
    "T_PRINT", "T_IDENT", "T_SEMICOLON",
    "T_RETURN", "T_SEMICOLON", "T_CLOSE_BRACE", "$"
]

# Executa o analisador
result = predictive_parser(tokens, M, "S")
if result:
    print("Success! Program belongs to the language.")
else:
    print("Error! Program does not belong to the language.")