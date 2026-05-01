from src.produtos import produtos

vendas = []


def calcular_venda(produto, quantidade):
    valor_bruto = produto["preco"] * quantidade

    desconto = 0
    if quantidade > 10:
        desconto = valor_bruto * 0.05

    valor_final = valor_bruto - desconto

    return valor_bruto, desconto, valor_final


def realizar_venda():
    if not produtos:
        print("Nenhum produto disponível.")
        return

    cliente = input("Nome do cliente: ").strip()
    if not cliente:
        print("Nome inválido.")
        return

    print("\nProdutos disponíveis:")
    for i, p in enumerate(produtos):
        print(f"{i + 1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")

    try:
        escolha = int(input("Selecione o produto (número): ")) - 1
        produto = produtos[escolha]
    except:
        print("Seleção inválida.")
        return

    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade deve ser maior que zero.")
            return
    except:
        print("Quantidade inválida.")
        return

    if quantidade > produto["estoque"]:
        print("Estoque insuficiente.")
        return

    valor_bruto, desconto, valor_final = calcular_venda(produto, quantidade)

    produto["estoque"] -= quantidade

    venda = {
        "cliente": cliente,
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }

    vendas.append(venda)

    print("Venda realizada com sucesso!")

def gerar_relatorio():
    if not vendas:
        print("Nenhuma venda realizada.")
        return

    total = 0

    print("\n=== Relatório de Vendas ===\n")

    for v in vendas:
        print(f"Cliente: {v['cliente']}")
        print(f"Produto: {v['produto']}")
        print(f"Quantidade: {v['quantidade']}")
        print(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        print(f"Desconto: R$ {v['desconto']:.2f}")
        print(f"Valor Final: R$ {v['valor_final']:.2f}")
        print()

        total += v["valor_final"]

    print(f"Total arrecadado: R$ {total:.2f}")


def salvar_relatorio():
    try:
        with open("relatorio_vendas.txt", "w", encoding="utf-8") as f:
            total = 0

            f.write("=== Relatório de Vendas ===\n\n")

            for v in vendas:
                f.write(f"Cliente: {v['cliente']}\n")
                f.write(f"Produto: {v['produto']}\n")
                f.write(f"Quantidade: {v['quantidade']}\n")
                f.write(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
                f.write(f"Desconto: R$ {v['desconto']:.2f}\n")
                f.write(f"Valor Final: R$ {v['valor_final']:.2f}\n\n")

                total += v["valor_final"]

            f.write(f"Total arrecadado: R$ {total:.2f}\n")

        print("Relatório salvo com sucesso!")

    except Exception as e:
        print("Erro ao salvar arquivo:", e)