#Exercício 6.1.

print("\nIdade em Dias\n")

def idadeDias():
    try:
        print("\nDigite o número de dias (inteiro positivo): \n")
        dias_totais = int(input())
        if dias_totais < 1:
            print("\nNúmero inválido! Digite um número inteiro positivo!\n")
        else:
            anos = dias_totais // 365  #Um ano com 365 dias
            dias_restantes = dias_totais % 365
            meses = dias_restantes // 30  #Um mês com 30 dias
            dias = dias_restantes % 30
            #Exibe o resultado
            print(f"\n{anos} ano(s)\n")
            print(f"\n{meses} mes(es)\n")
            print(f"\n{dias} dia(s)\n")

    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

idadeDias()

#Exercício 6.2.

print("\nAumento de Salário\n")

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

#Exercício 6.3.

print("\nValidação de Nota\n")

def validacao_nota():
    try:
        n1 = -1
        n2 = -1
        while n1 < 0:
            print("\nDigite a primeira nota do aluno: \n")
            n1 = float(input())
            if n1 < 0:
                print("\nNota inválida!\n")
            elif n1 > 10:
                while n1 > 10:
                    print("\nNota inválida!\n")
                    print("\nDigite a primeira nota do aluno: \n")
                    n1 = float(input())
                    if n1 < 0:
                        print("\nNota inválida!\n")
                
        while n2 < 0:
            print("\nDigite a segunda nota do aluno: \n")
            n2 = float(input())
            if n2 < 0:
                print("\nNota inválida!\n")
            elif n2 > 10:
                while n2 > 10:
                    print("\nNota inválida!\n")
                    print("\nDigite a segunda nota do aluno: \n")
                    n2 = float(input())
                    if n2 < 0:
                        print("\nNota inválida!\n")
                  
        media = (n1 + n2) / 2
        print(f"\nMédia: {media:.1f}\n")

    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

validacao_nota()


#Exercício 6.4.

print("\nQuadrante\n")

def determinar_quadrante():
    
    try:

        while True:
            
            x = int(input("Digite o valor de x (ou 0 para sair): "))
            y = int(input("Digite o valor de y (ou 0 para sair): "))
            
            # Verifica a condição de saída
            if x == 0 or y == 0:
                print("\nCoordenada com x ou y nulo. Encerrando o programa\n")
                break

            # Determina o quadrante
            if x > 0 and y > 0:
                print("\nPrimeiro quadrante\n")
            elif x < 0 and y > 0:
                print("\nSegundo quadrante\n")
            elif x < 0 and y < 0:
                print("\nTerceiro quadrante\n")
            elif x > 0 and y < 0:
                print("\nQuarto quadrante\n")
            # else:
            #     print("Erro inesperado.")  # Apenas uma verificação adicional
    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

determinar_quadrante()

#Exercício 6.5.

print("\nSequência Lógica 2\n")

def imprimir_sequencia():
    
    try:

        x = int(input("\nDigite o valor de x (inteiro, sendo 1 < x < 20): \n"))
        y = int(input("\nDigite o valor de y (inteiro, sendo x < y < 100000): \n"))
        print()

        # Verifica as condições de validade
        if not (1 < x < 20):
            print("\nO valor de x deve ser maior do que 1 e menor do que 20!\n")
            return
        if not (x < y < 100000):
            print("\nO valor de y deve ser maior do que x e menor do que 100000!\n")
            return

        # Imprime a sequência
        for i in range(1, y + 1):
            # Imprime os números na linha atual, separados por espaço
            print(i, end=" ")
            # Adiciona uma quebra de linha a cada x números
            if i % x == 0:
                print()
    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

imprimir_sequencia()

#Exercício 6.6.

print("\nLeitura de Arquivo e Operações com Números\n")

def leitura_arquivo():
    import os
    
    try:
        # Solicita o nome do arquivo ao usuário (não são aceitas extensões da Microsoft, só com a importação da biblioteca python-docx)

        nome_arquivo = input("\nDigite o nome do arquivo (com extensão): \n")
        
        # Exibe o diretório atual, usando a biblioteca OS: o arquivo deve estar dentro dele. Caso contrário, deve ser digitado o endereço do mesmo.

        print(f"\nProcurando o arquivo em: {os.getcwd()}\n")

        # Abre o arquivo e lê os números
        
        with open(nome_arquivo, 'r') as arquivo:
            numeros = [int(linha.strip()) for linha in arquivo]
        
        # Calcula os resultados
        soma = sum(numeros)
        media = soma / len(numeros)
        maior = max(numeros)
        menor = min(numeros)

        # Exibe os resultados
        print(f"\nSoma: {soma}\n")
        print(f"\nMédia: {media:.2f}\n")
        print(f"\nMaior número: {maior}\n")
        print(f"\nMenor número: {menor}\n")

    except FileNotFoundError:
        print("\nArquivo não encontrado. Verifique o nome e tente novamente!\n")
    except ValueError:
        print("\nO arquivo contém dados inválidos. Certifique-se de que há apenas números inteiros!\n")
    except ZeroDivisionError:
        print("\nO arquivo está vazio. Não é possível calcular os valores!\n")

leitura_arquivo()
