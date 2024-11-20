#Exercício 2.1.

print("\nDiferença\n")

def diferenca():
    A = int(input("Digite o primeiro número inteiro: "))
    B = int(input("Digite o segundo número inteiro: "))
    C = int(input("Digite o terceiro número inteiro: "))
    D = int(input("Digite o quarto número inteiro: "))
    DIFERENCA = (A * B) - (C * D)
    print(f"Diferença = {DIFERENCA}")
   
diferenca()

#Exercício 2.2.

print("\nSalário\n")

def salario():
    NUMBER = int(input("Digite o número do funcionário: "))
    HOURS = int(input("Digite o número de horas trabalhadas: "))
    HOURS_SALARY = float(input("Digite o salário por hora de trabalho: "))
    SALARY = HOURS * HOURS_SALARY
    print(f"NUMBER = {NUMBER}")
    print(f"SALARY = U$ {SALARY:.2f}")

salario()

#Exercício 2.3.

print("\nSalário com bônus\n")

def bonus():
    NOME = input("Digite o primeiro nome do vendedor: ")
    SALARIO_FIXO = float(input("Digite o salário fixo do vendedor: "))
    TOTAL_VENDAS = float(input("Digite o total em dinheiro de vendas efetuadas: "))
    TOTAL = SALARIO_FIXO + (0.15 * TOTAL_VENDAS)
    print("Nome = " + NOME)
    print(f"TOTAL = R$ {TOTAL:.2f}")

bonus()

#Exercício 2.4.

print("\nCálculo simples\n")

def calc_simples():
    codigo_peca1, quantidade_peca1, valor_peca1 = input("Digite o código, quantidade e valor da peça 1 (separados por espaço): ").split()
    codigo_peca1 = int(codigo_peca1)
    quantidade_peca1 = int(quantidade_peca1)
    valor_peca1 = float(valor_peca1)

    codigo_peca2, quantidade_peca2, valor_peca2 = input("Digite o código, quantidade e valor da peça 2 (separados por espaço): ").split()
    codigo_peca2 = int(codigo_peca2)
    quantidade_peca2 = int(quantidade_peca2)
    valor_peca2 = float(valor_peca2)

    valor_total = (quantidade_peca1 * valor_peca1) + (quantidade_peca2 * valor_peca2)

    print(f"Valor total a pagar: R$ {valor_total:.2f}")

calc_simples()

#Exercício 2.5.

print("\nDistância entre dois pontos\n")

def dist_coord():
    #Coordenada ponto 1

    print("Entre com o valor do ponto 1 (separado por espaço): ")
    x1, y1 = map(float, input().split())

    #Coordenada ponto 2

    print("Entre como valor do ponto 2 (separado por espaço): ")
    x2, y2 = map(float, input().split())

    #Cálculo da fórmula

    distancia = ((x2 - x1)** 2 + (y2-y1)** 2) ** 0.5

    #Exibir a distância segundo a fórmula

    print(f"A distância é igual a: {distancia:.4f}")

dist_coord()

print("\nFIM!\n")