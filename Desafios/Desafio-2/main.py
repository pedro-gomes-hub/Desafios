from src.produtos import cadastrar_produto
from src.vendas import realizar_venda, gerar_relatorio, salvar_relatorio


def menu():
    while True:
        print("\n=== MENU ===")
        print("1 - Cadastrar produto")
        print("2 - Realizar venda")
        print("3 - Gerar relatório")
        print("4 - Salvar relatório")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            realizar_venda()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            salvar_relatorio()
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")


if __name__ == "__main__":
    menu()