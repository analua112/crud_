import csv
from perfume import Perfume

def escreveArquivo(nome, fragrancia, volume, preco, dataFabricacao, embalagem):
    with open('Perfumes.csv', 'a', newline='', encoding='utf-8', errors='ignore') as csvfile:
        escreve = csv.writer(csvfile, delimiter=',')
        escreve.writerow([nome, fragrancia, volume, preco, dataFabricacao, embalagem])
        print("### PERFUME ", nome, "ADICIONADO COM SUCESSO!! ###")
        
perfumes = []
def abrir():
    print("### BEM VINDO A TELA DE CADASTRO DE PERFUMES ###")
    print("\nNOVO PERFUME: ")
    nome = input("NOME: \n")
    fragrancia = input("FRAGRANCIA:  \n")
    volume = input("VOLUME: \n")
    preco = input("PREÇO: \n")
    dataFabricacao = input("DATA DE FABRICAÇAO: \n")
    embalagem = input("TIPO: \n")
    novoPerfume = Perfume(nome, fragrancia, volume, preco, dataFabricacao, embalagem)

    escreveArquivo(nome, fragrancia, volume, preco, dataFabricacao, embalagem)
    perfumes.append(novoPerfume)