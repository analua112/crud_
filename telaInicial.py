import telaCadastro
import telaLeitura
import telaExclusao
import telaAtualizar

while(True):
    print("### MENU PRINCIPAL ###")
    print("1 - CADASTRAR")
    print("2 - VER ESTOQUE")
    print("3 - EXCLUIR")
    print("4 - ATUALIZAR")
    opcao = int(input("Digite a opção desejada:"))
    if opcao == 1:
        telaCadastro.abrir()
    elif opcao == 2:
        telaLeitura.abrir()
    elif opcao == 3:
        telaExclusao.abrir()
    elif opcao == 4:
        telaAtualizar.abrir()
    else:
        print("Opção inválida")


# CRUD = CREATE, READ, UPDATE, DELETE.
# 1 - cadastrar
# 2 - ler
# 3 - atualizar
# 4 - deletar