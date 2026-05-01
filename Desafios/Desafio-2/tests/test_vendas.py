from src.vendas import calcular_venda

def test_calculo_sem_desconto():
    produto = {"nome": "Item", "preco": 10.0, "estoque": 100}

    bruto, desconto, final = calcular_venda(produto, 5)

    assert bruto == 50
    assert desconto == 0
    assert final == 50


def test_calculo_com_desconto():
    produto = {"nome": "Item", "preco": 10.0, "estoque": 100}

    bruto, desconto, final = calcular_venda(produto, 15)

    assert bruto == 150
    assert desconto == 7.5
    assert final == 142.5