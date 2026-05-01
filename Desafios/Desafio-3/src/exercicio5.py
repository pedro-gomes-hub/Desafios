import numpy as np

def executar():
    estoque = [
        [1, 2],
        [3, 4]
    ]

    precos = [
        [10, 20],
        [30, 40]
    ]

    m1 = np.array(estoque)
    m2 = np.array(precos)

    transposta = m1.T
    resultado = transposta @ m2

    return transposta, resultado