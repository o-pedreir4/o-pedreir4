# Programa de Pesquisa de Satisfação - TudoWeb
# Estrutura de repetição para coletar dados de atendimento

qtd_excelente = 0
qtd_bom = 0
qtd_ruim = 0
TOTAL_ENTREVISTADOS = 50
print("--- PESQUISA DE SATISFAÇÃO TUDOWEB ---")
for i in range(1, TOTAL_ENTREVISTADOS + 1):
    print(f"\nEntrevistado nº {i}") 
    nome = input("Digite o nome: ")
    idade = int(input("Digite a idade: "))
    print("Opinião sobre o atendimento: ")
    print("1: EXCELENTE | 2: BOM | 3: RUIM")
    opiniao = input("Escolha a opção (1, 2 ou 3): ")
    if opiniao == "1":
        qtd_excelente += 1
    elif opiniao == "2":
        qtd_bom += 1
    elif opiniao == "3":
        qtd_ruim += 1
    else:
        print("Opção inválida! Este voto não será contabilizado.")
print("\n" + "="*50)
print("RESULTADO DA PESQUISA")
print("="*50)
print(f"a) Quantidade de respostas 'EXCELENTE': {qtd_excelente}")
print(f"b) Quantidade de respostas 'RUIM': {qtd_ruim}")
print(f"Total de respostas 'BOM': {qtd_bom}")
print(f"Total de pessoas entrevistadas: {TOTAL_ENTREVISTADOS}")
