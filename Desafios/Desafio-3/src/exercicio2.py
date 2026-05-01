def somar_matrizes(A, B):
    linhas = len(A)
    colunas = len(A[0])

    resultado = [[0 for _ in range(colunas)] for _ in range(linhas)]

    for i in range(linhas):
        for j in range(colunas):
            resultado[i][j] = A[i][j] + B[i][j]

    return resultado


def executar():
    A = [[1, 2], [3, 4]]
    B = [[5, 6], [7, 8]]
    return somar_matrizes(A, B)