def ex1():
    import os
    import csv

    pasta = "Banco/Caninos"
    coluna_alvo = "Nome"

    # Obtém a lista de arquivos na pasta
    arquivos = os.listdir(pasta)

    # Lista para armazenar os valores da coluna alvo
    valores_coluna = []

    # Itera sobre cada arquivo na lista
    for arquivo in arquivos:
        # Verifica se o item é um arquivo CSV
        if arquivo.endswith(".csv"):
            # Abre o arquivo CSV
            with open(os.path.join(pasta, arquivo), 'r') as f:
                reader = csv.DictReader(f)
                # Obtém os valores da coluna alvo e adiciona à lista
                for row in reader:
                    valor = row[coluna_alvo]
                    valores_coluna.append(valor)

    # Imprime os valores da coluna alvo
    print(valores_coluna)


def ex2(tipo):
    import os
    import csv

    pasta = f"Banco/{tipo}"
    coluna_alvo = "Nome"
    arquivos = os.listdir(pasta)
    pilha_valores = []

    for arquivo in arquivos:
        if arquivo.endswith(".csv"):
            with open(os.path.join(pasta, arquivo), 'r') as f:
                reader = csv.DictReader(f)
                # Obtém os valores da coluna alvo e adiciona à pilha
                for row in reader:
                    valor = row[coluna_alvo]
                    pilha_valores.append(valor)

    # Imprime os valores da coluna alvo (desempilhando)
    while not len(pilha_valores) == 0:
        valor = pilha_valores.pop()
        print(valor)


ex2('Caninos')
