import random

def gerar_matriz_zeros(linhas, colunas):
    return [[0 for _ in range(colunas)] for _ in range(linhas)]

def preencher_aleatorio(matriz, inicio=0, fim=10):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            matriz[i][j] = random.randint(inicio, fim)
    return matriz