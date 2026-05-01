produtos = []

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if not nome:
        print("Nome não pode ser vazio.")
        return

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            print("Produto já cadastrado.")
            return

    try:
        preco = float(input("Preço: "))
        if preco <= 0:
            print("Preço deve ser maior que zero.")
            return
    except:
        print("Preço inválido.")
        return

    try:
        estoque = int(input("Estoque inicial: "))
        if estoque < 0:
            print("Estoque não pode ser negativo.")
            return
    except:
        print("Estoque inválido.")
        return

    produtos.append({
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    })

    print("Produto cadastrado com sucesso!")


def listar_produtos():
    if not produtos:
        print("Nenhum produto cadastrado.")
        return

    for i, p in enumerate(produtos):
        print(f"{i + 1}. {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")