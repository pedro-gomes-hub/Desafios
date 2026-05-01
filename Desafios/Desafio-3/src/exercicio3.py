import numpy as np

def executar():
    alunos = [
        [7, 8, 9],
        [5, 7, 9],
        [10, 8, 9]
    ]

    matriz = np.array(alunos)
    medias = matriz.mean(axis=1)

    medias = medias.astype(int)

    return medias