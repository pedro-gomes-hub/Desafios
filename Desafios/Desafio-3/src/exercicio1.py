from utils.helpers import gerar_matriz_zeros, preencher_aleatorio

def executar():
    matriz = gerar_matriz_zeros(3, 3)
    matriz = preencher_aleatorio(matriz)
    return matriz