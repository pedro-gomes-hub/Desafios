from src import exercicio1, exercicio2, exercicio3, exercicio4, exercicio5

def main():
    print("=== EXERCÍCIO 1 ===")
    print(exercicio1.executar())

    print("\n=== EXERCÍCIO 2 ===")
    print(exercicio2.executar())

    print("\n=== EXERCÍCIO 3 ===")
    print(exercicio3.executar())

    print("\n=== EXERCÍCIO 4 ===")
    det, solucao = exercicio4.executar()
    print("Determinante:", det)
    print("Tem solução?", solucao)

    print("\n=== EXERCÍCIO 5 ===")
    transposta, resultado = exercicio5.executar()
    print("Transposta:")
    print(transposta)
    print("Resultado:")
    print(resultado)


if __name__ == "__main__":
    main()