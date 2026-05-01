from src.calculos import calcular_clt, calcular_estagiario, calcular_freelancer

def testar_sistema():
    print("=== Iniciando Testes de Cálculo ===\n")

    # Teste CLT
    inss, irrf, liquido = calcular_clt(3000)
    print(f"[CLT] Líquido: {liquido}")
    assert liquido == 2460

    # Teste Estagiário
    inss, irrf, liquido = calcular_estagiario(1000)
    print(f"[ESTÁGIO] Líquido: {liquido}")
    assert liquido == 1000

    # Teste Freelancer - CORRIGIDO AQUI (3 variáveis)
    desconto, irrf_vazio, liquido = calcular_freelancer(50, 40)
    print(f"[FREE] Líquido: {liquido}")
    assert liquido == 1900

    print("\n[SUCESSO] Todos os testes passaram!")

if __name__ == "__main__":
    testar_sistema()