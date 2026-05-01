def obter_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor > 0: return valor
            print("Erro: O valor deve ser maior que zero.")
        except ValueError:
            print("Erro: Digite um número válido.")