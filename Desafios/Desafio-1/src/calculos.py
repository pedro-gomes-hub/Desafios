def calcular_estagiario(bruto):
    # Retorna: INSS, IRRF, Líquido
    return 0.0, 0.0, bruto 

def calcular_clt(bruto):
    inss = bruto * 0.08
    irrf = bruto * 0.10 if bruto > 2000 else 0.0
    liquido = bruto - inss - irrf
    # Retorna: INSS, IRRF, Líquido
    return inss, irrf, liquido

def calcular_freelancer(valor_hora, horas):
    bruto = valor_hora * horas
    desconto = bruto * 0.05
    liquido = bruto - desconto
    # Retorna: Desconto, IRRF(vazio), Líquido
    # Isso resolve o erro de "unpack"
    return desconto, 0.0, liquido