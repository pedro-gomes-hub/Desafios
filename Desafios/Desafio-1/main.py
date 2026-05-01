import os
from utils.validacoes import obter_valor
from src.processamento import processar_salario

def gerar_relatorio(funcionarios):
    texto = "=== Relatório de Folha de Pagamento ===\n"
    total_empresa = 0
    for f in funcionarios:
        texto += f"Nome: {f['nome']}\n"
        texto += f"Tipo: {f['tipo'].capitalize()}\n"
        texto += f"Salário Bruto: R$ {f['bruto']:.2f}\n"
        texto += f"Desconto INSS: R$ {f['inss']:.2f}\n"
        texto += f"Desconto IRRF: R$ {f['irrf']:.2f}\n"
        texto += f"Salário Líquido: R$ {f['liquido']:.2f}\n"
        texto += "-" * 30 + "\n"
        total_empresa += f['liquido']
    texto += f"Total pago pela empresa: R$ {total_empresa:.2f}\n"
    return texto

def salvar_relatorio(texto):
    os.makedirs("relatorios", exist_ok=True)
    caminho = "relatorios/relatorio_folha.txt"
    try:
        with open(caminho, "w", encoding="utf-8") as arq:
            arq.write(texto)
        print(f"\n[Sucesso] Relatório salvo em: {caminho}")
    except IOError as e:
        print(f"\n [Erro] Falha ao salvar arquivo: {e}")

def main():
    funcionarios = []

    while True:
        print("\n" + "="*40)
        print("Sistema de Folha de Pagamento da Empresa")
        print("="*40)
        print("1. Cadastrar | 2. Relatório | 3. Salvar | 4. Sair")
        opcao = input("Escolha: ")

        if opcao == '1':
            nome = input("Nome: ").strip()
            tipo = input("Tipo (estagiario, clt, freelancer): ").strip().lower()

            if not nome or tipo not in ['estagiario', 'clt', 'freelancer']:
                print("\n [Erro] Nome vazio ou tipo inválido!")
                continue

            if tipo == 'freelancer':
                v = obter_valor("Valor por hora: ")
                h = obter_valor("Horas trabalhadas: ")
                f_dados = processar_salario(nome, tipo, valor_hora=v, horas=h)
            else:
                s = obter_valor("Salário bruto: ")
                f_dados = processar_salario(nome, tipo, salario=s)

            funcionarios.append(f_dados)
            print(f"\n [Sucesso] {nome} cadastrado com sucesso!")

        elif opcao == '2':
            if not funcionarios:
                print("\n [Aviso] Nenhum funcionário cadastrado.")
            else:
                print("\n" + gerar_relatorio(funcionarios))

        elif opcao == '3':
            if not funcionarios:
                print("\n [Aviso] Nenhum funcionário cadastrado para salvar.")
            else:
                relatorio = gerar_relatorio(funcionarios)
                salvar_relatorio(relatorio)

        elif opcao == '4':
            print("\n Saindo do programa... Até logo!")
            break

        else:
            print("\n Erro:Opção inválida! Escolha entre 1 e 4.")

if __name__ == "__main__":
    main()