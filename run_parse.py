# Bruno Vazquez Lafaiete (20102277), Guilherme Cassiano Ferreira Silva (23250871), Victor Luiz de Souza (21105576)

import os
import lexer_parte_b as lexer
from parser import predictive_parser, M

def listar_arquivos(diretorio):
    arquivos = [f for f in os.listdir(diretorio) if os.path.isfile(os.path.join(diretorio, f))]
    return arquivos

def selecionar_arquivo(arquivos):
    print("Deseja executar qual arquivo?")
    for i, arquivo in enumerate(arquivos):
        print(f"{i + 1}. {arquivo}")
    escolha = int(input("Digite o número do arquivo desejado: ")) - 1
    if 0 <= escolha < len(arquivos):
        return arquivos[escolha]
    else:
        print("Escolha inválida.")
        return None

def main():
    diretorio = os.path.expanduser("./test-sources")  # Caminho relativo ao diretório home do usuário
    arquivos = listar_arquivos(diretorio)
    if not arquivos:
        print("Nenhum arquivo encontrado no diretório.")
        return

    arquivo_escolhido = selecionar_arquivo(arquivos)
    if arquivo_escolhido:
        caminho_arquivo = os.path.join(diretorio, arquivo_escolhido)
        if not os.path.isfile(caminho_arquivo):
            print(f"Arquivo '{caminho_arquivo}' não encontrado.")
        else:
            tokens = lexer.get_tokens(caminho_arquivo)
            print(tokens)
            result = predictive_parser(tokens, M, "S")
            if result:
                print("Success! Program belongs to the language.")
            else:
                print("Error! Program does not belong to the language.")

if __name__ == "__main__":
    main()