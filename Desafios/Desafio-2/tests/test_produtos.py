from src.produtos import produtos

def test_cadastro_produto():
    produtos.clear()

    produtos.append({
        "nome": "Teste",
        "preco": 10.0,
        "estoque": 5
    })

    assert len(produtos) == 1
    assert produtos[0]["nome"] == "Teste"