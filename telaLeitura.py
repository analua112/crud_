import csv
def abrir():
    i = 0
    with open('Perfumes.csv', newline='', encoding='utf-8', errors='ignore') as csvfile:
        leitor = csv.reader(csvfile, delimiter=',')
        for linha in leitor: 
            print(f"Perfume {i}: NOME: {linha[0]}, FRAGANCIA: {linha[1]}, VOLUME: {linha[2]}, PREÇO: R${linha[3]}, DATA/FABRICAÇAO: {linha[4]}  ")
            i = i+1