# Ler a base de dados (arquivo)
# Utilizar classe para alterar os dados
# Receber o indice da camiseta a ser atualizada
# Atualizar os dados na classe
def abrir():
    import csv 
    from perfume import Perfume
    perfumes = []

    def ler_arquivo():
        with open('Perfumes.csv', newline='', encoding='utf-8', errors='ignore') as csvLeitura:
            linha = csv.reader(csvLeitura, delimiter= ',')
            for coluna in linha:
            # ARMAZENAR PRODUTOS DE UMA LISTA
                novoPerfume = Perfume(coluna[0], coluna[1], coluna[2], coluna[3], coluna[4], coluna[5])
                perfumes.append(novoPerfume)

    def altera_dados():
        indice = int(input("Digite o indice da camiseta a ser alterado: "))
        print("digite apenas o atributo que deseja alterar, caso contrario apenas aperte ENTER.")
        nome = input("Nome: ")
        fragrancia = input("fragancia: ")
        volume = input("volume: ")
        preco = input("preco: ")
        dataFabricacao = input("data de fabricaçao: ")
        embalagem = input("embalagem: ")
        if nome != "":
            perfumes[indice].nome = nome 
        if fragrancia != "":
            perfumes[indice].fragrancia = fragrancia 
        if volume != "":
            perfumes[indice].volume = volume
        if preco != "":
            perfumes[indice].preco = preco
        if dataFabricacao != "":
            perfumes[indice].dataFabricacao = dataFabricacao
        if embalagem != "":
            perfumes[indice].embalagem = embalagem

    def escreveArquivo():
        with open('Perfumes.csv', 'w', newline='', encoding='utf-8', errors='ignore') as csvEscrita:
            escrever = csv.writer(csvEscrita)
            for p in perfumes:
                escrever.writerow([p.nome, p.fragrancia, p.volume, p.preco, p.dataFabricacao, p.embalagem])
            print(f"Arquivo atualizado! Perfumes atualizados com sucesso!")

    ler_arquivo()
    altera_dados()
    escreveArquivo()