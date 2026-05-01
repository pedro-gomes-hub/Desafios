import numpy as np

def executar():
    matriz = [
        [1, 2, 3],
        [0, 1, 4],
        [5, 6, 0]
    ]

    matriz_np = np.array(matriz)

    det = np.linalg.det(matriz_np)

    det = int(round(det))

    tem_solucao = det != 0

    return det, tem_solucao