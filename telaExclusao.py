import csv
linhas = []
def abrir():
    indice = int(input("digite o numero da camiseta a ser excluido: "))

    # LER ARQUIVO DE PRODUTOS
    with open('Perfumes.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
        leitor = csv.reader(csvLeitura, delimiter= ',')
        for linha in leitor:
            # ARMAZENAR PRODUTOS DE UMA LISTA
            linhas.append(linha)

            # REMOVER O "INDICE" DA LISTA
            linhas.pop(indice)
            #print(linhas)

    # REESCREVER O ARQUIVO COM A LISTA ATUALIZADA
    with open('Perfumes.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
        escrever = csv.writer(csvEscrita)
        escrever.writerows(linhas)
        print(f"Arquivo Atualizado! Perfume {indice} excluida com sucesso!")