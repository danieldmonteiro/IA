#Exercício 3.1.

print("\nIntervalo\n")

def main():
    
    print("\nEntre com o valor: \n")
    valor = float(input())

    if 0 <= valor <= 25:
        if valor == 25:
            print("\nO número está nos intervalos [0, 25] e [25, 50]\n")
        else: 
            print("\nO número está no intervalo [0,25]\n")
    elif 25 < valor <= 50:
        if valor == 50:
            print("\nO número está nos intervalos [25, 50] e [50, 75]\n")
        else: 
            print("\nO número está no intervalo [25, 50]\n")
    elif 50 < valor <= 75:
        if valor == 75:
            print("\nO número está nos intervalos [50, 75] e [75, 100]\n")
        else: 
            print("\nO número está no intervalo [50, 75]\n")
    elif 75 < valor <= 100:
        print("\nO número está no intervalo [75, 100]\n")
    else:
        print("\nFora dos intervalos\n")

main()

print("\nFIM!\n")

#Exercício 3.2.

print("\nLanche\n")

def lanche():

    print("\nDigite o código do produto: \n")
    codigo = int(input())
    print("\nDigite a quantidade de produtos: \n")
    quantidade = int(input())

    if codigo == 1:
        print(f"\nTotal: R$ {quantidade * 4:.2f}\n")
    elif codigo == 2:
        print(f"\nTotal: R$ {quantidade * 4.5:.2f}\n")
    elif codigo == 3:
        print(f"\nTotal: R$ {quantidade * 5:.2f}\n")
    elif codigo == 4:
        print(f"\nTotal: R$ {quantidade * 2:.2f}\n")
    elif codigo == 5:
        print(f"\nTotal: R$ {quantidade * 1.5:.2f}\n")
    else:
        print("\nCódigo inválido!\n")
    

lanche()

# Exercício 3.3.

print("\nAumento de salário\n")

def aumentoSalario():

    print("\nDigite o valor do salário atual: \n")
    salarioAtual = float(input())
    if 0 <= salarioAtual <= 400:
        novoSalario = salarioAtual * 1.15
        print(f"\nNovo salário: R$ {novoSalario:.2f}\n")
        print(f"\nReajuste ganho: R$ {(novoSalario - salarioAtual):.2f}\n")
        print("\nEm percentual: 15%\n")
    elif 400.01 <= salarioAtual <= 800:
        novoSalario = salarioAtual * 1.12
        print(f"\nNovo salário: R$ {novoSalario:.2f}\n")
        print(f"\nReajuste ganho: R$ {(novoSalario - salarioAtual):.2f}\n")
        print("\nEm percentual: 12%\n")
    elif 800.01 <= salarioAtual <= 1200:
        novoSalario = salarioAtual * 1.10
        print(f"\nNovo salário: R$ {novoSalario:.2f}\n")
        print(f"\nReajuste ganho: R$ {(novoSalario - salarioAtual):.2f}\n")
        print("\nEm percentual: 10%\n")
    elif 1200.01 <= salarioAtual <= 2000:
        novoSalario = salarioAtual * 1.07
        print(f"\nNovo salário: R$ {novoSalario:.2f}\n")
        print(f"\nReajuste ganho: R$ {(novoSalario - salarioAtual):.2f}\n")
        print("\nEm percentual: 7%\n")
    elif 2000 < salarioAtual:
        novoSalario = salarioAtual * 1.04
        print(f"\nNovo salário: R$ {novoSalario:.2f}\n")
        print(f"\nReajuste ganho: R$ {(novoSalario - salarioAtual):.2f}\n")
        print("\nEm percentual: 4%\n")
    else:
        print("Valor inválido!")

aumentoSalario()

#Exercício 3.4.

print("\nTeste de Seleção 1\n")

def testeSel1():
    print("\nDigite quatro números inteiro (separados por espaço): \n")
    A, B, C, D = map(int, input().split())

    if B > C and D > A and (C + D) > (A + B) and C >= 0 and D >= 0 and A % 2 == 0:
        print("\nValores aceitos!\n")
    else:
        print("\nValores não aceiros!\n")

testeSel1()

#Exercício 3.5.

print("\nMédia 3\n")

def calcMedia():
    print("\nDigite as quatro notas (separados por espaço): \n")
    N1, N2, N3, N4 = map(float, input().split())
    peso1, peso2, peso3, peso4 = 2, 3, 4, 1
    media_ponderada = (N1 * peso1 + N2 * peso2 + N3 * peso3 + N4 * peso4) / (peso1 + peso2 + peso3 + peso4)
    print(f"\nMédia: {media_ponderada:.1f}\n")
    if media_ponderada >= 7:
        print("\nAluno aprovado!\n")
    elif media_ponderada < 5:
        print("\nAluno reprovado!\n")
    else:
        print("\nAluno em exame!\n")
        print("\nQual a nota do exame?\n")
        notaExame = float(input())
        notaFinal = (notaExame + media_ponderada)/2
        print(f"\nNota do exame: {notaExame:.1f}\n")
        if notaFinal >= 5:
            print("\nAluno aprovado!\n")
        else:
            print("\nAluno reprovado!\n")
        print(f"\nMédia final: {notaFinal:.1f}\n")

calcMedia()