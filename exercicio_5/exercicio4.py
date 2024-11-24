#Exercício 5.1.

print("\nSequência Lógica\n")

def sequencia_logica():
    
    try:
        print("\nDigite um número inteiro positivo: \n")
        N = int(input())
        if N < 1:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 1000!\n")
        elif N > 1000:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 1000!\n")
        else:
            linhas = N * 2
            for i in range(1, linhas + 1):
                a = (i + 1) // 2  # Determina o valor de a (repetido a cada 2 linhas)
        
                if i % 2 != 0:  # Linha ímpar: padrão b1, c1
                    b = a**2
                    c = a**3
                else:  # Linha par: padrão b2, c2
                    b = a**2 + 1
                    c = a**3 + 1
                print()
                print(f"{a} {b} {c}")

    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

sequencia_logica()

#Exercício 5.2.

print("\nFibonacci Fácil\n")

def fibonacci():
    try:
        print("\nDigite a quantidade de números da sequência Fibonacci que serão exibidos: \n")
        N = int(input())
        sequeFibo = []
        if N < 1:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 46!\n")
        elif N > 46:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 46!\n")
        else:
            A, B = 0, 1
            for _ in range(N):
                sequeFibo.append(A)
                A, B = B, A + B
            print()
            print(" ".join(map(str, sequeFibo)))
            print()
    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

fibonacci()

#Exercício 5.3.

print("\nFatorial Simples\n")

def fatorial_simples():
    try:
        print("\nDigite o número inteiro e positivo para calcular o fatorial: \n")
        N = int(input())
        
        if N < 1:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 13!\n")
        elif N >= 13:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 13!\n")
        else:
            fatorial = 1
            for i in range(1, N + 1):
                fatorial *= i
            print(f"\nFatorial = {fatorial}\n")
            
    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

fatorial_simples()

#Exercício 5.4.

print("\nIdades\n")

def idades():
    import random
    quantidade = random.randint(5, 20)
    idades = [random.randint(0, 100) for _ in range(quantidade)]
    media_idades = sum(idades) / quantidade
    idades_como_string = " ".join(map(str, idades))
    print(f"\nA lista de idades gerada é: {idades_como_string}\n")
    print(f"\nA média das idade é: {media_idades:.2f}\n")
idades()

#Exercício 5.5.

print("\nCrescimento Populacional\n")

def crescimento_pop():
    
    try:
        print("\nDigite o número de casos de teste: \n")
        T = int(input())
        
        if T < 1:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 3000!\n")
        elif T > 3000:
            print("\nNúmero inválido! Digite um número inteiro positivo e menor do que 3000!\n")
        else:
            for _ in range(T):
                print("\nDigite a população da cidade A (número inteiro), a população da cidade B (número inteiro), o crescimento populacional percentual da cidade A (com uma casa decimal) e o crescimento populacional percentual da cidade B (com uma casa decimal) separados por espaço:  \n")
                entrada = input().split()
                pa = int(entrada[0])  # População da cidade A
                pb = int(entrada[1])  # População da cidade B
                g1 = float(entrada[2])  # Crescimento populacional da cidade A (%)
                g2 = float(entrada[3])  # Crescimento populacional da cidade B (%)
                anos = 0
                if pa < 100:
                    print("\nA população da cidade A deve ser maior ou igual a 100 e menor do que 1000.000!\n")
                    break
                elif pa >= 1000000:
                    print("\nA população da cidade A deve ser maior ou igual a 100 e menor do que 1000.000!\n")
                    break
                elif pb > 1000000:
                    print("\nA população da cidade B não pode ser maior do que 1000.000!\n")
                    break
                elif pb <= pa:
                    print("\nA população da cidade B tem que ser maior do que a população da cidade A!\n")
                    break
                elif g1 < 0.1:
                    print("\nO crescimento populacional percentual da cidade A não pode ser menor do que 0.1!\n")
                    break
                elif g1 > 10:
                    print("\nO crescimento populacional percentual da cidade A não pode ser maior do que 10!\n")
                    break
                elif g1 <= g2:
                    print("\nO crescimento populacional percentual da cidade A não pode ser menor ou igual ao crescimento populacional da cidade B!\n")
                    break
                elif g2 < 0:
                    print("\nO crescimento populacional percentual da cidade B não pode ser menor do que 0!\n")
                    break
                
                
                # Calcula o crescimento ano a ano
                while pa <= pb:
                    pa += int(pa * (g1 / 100))
                    pb += int(pb * (g2 / 100))
                    anos += 1

                    # Verifica se ultrapassa 100 anos
                    if anos > 100:
                        print("\nVai demorar mais de um século!\n")
                        break

                # Caso A supere B antes de 100 anos
                if anos <= 100:
                    print(f"\nVai demorar {anos} anos!\n")
    except ValueError:
        print("\nVocê digitou um caracter inválido!\n")

crescimento_pop()
