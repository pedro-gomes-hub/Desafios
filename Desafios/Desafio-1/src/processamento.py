from src.calculos import calcular_estagiario, calcular_clt, calcular_freelancer

def processar_salario(nome, tipo, **kwargs):
    if tipo == 'estagiario':
        bruto = kwargs.get('salario')
        inss, irrf, liquido = calcular_estagiario(bruto)
    elif tipo == 'clt':
        bruto = kwargs.get('salario')
        inss, irrf, liquido = calcular_clt(bruto)
    elif tipo == 'freelancer':
        v_hora = kwargs.get('valor_hora')
        hrs = kwargs.get('horas')
        bruto = v_hora * hrs
        # Agora o freelancer também devolve 3 valores
        inss, irrf, liquido = calcular_freelancer(v_hora, hrs)
    
    return {
        "nome": nome, 
        "tipo": tipo.capitalize(), 
        "bruto": bruto,
        "inss": inss, 
        "irrf": irrf, 
        "liquido": liquido
    }