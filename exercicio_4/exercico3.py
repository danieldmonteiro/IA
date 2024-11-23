#Exercício 4.1.

print("\nSequência IJ 1\n")

def sequencia_ij1():
    I = 1
    J = 60
    while  0 <= J <=60 and I >= 1:
        print(f"I = {I}  J = {J}")
        I += 3
        J -= 5

sequencia_ij1()

#Exercício 4.2.

print("\nMaior e Posição\n")

def maior_posicao():
    import random
    numeros = random.sample(range(1, 1001), 100)
    maior_valor = max(numeros)
    posicao = numeros.index(maior_valor) + 1
    print(f"\nA lista gerada é: {numeros}\n")
    print(f"\nO maior valor é {maior_valor} e está na posição {posicao} da lista.\n")
maior_posicao()

#Exercício 4.3.

print("\nSoma de Ímpares consecutivos II\n")

def somaImpares():
    try:
        N = int(input("\nDigite o número de casos de teste: \n"))
        if N < 1:
            print("\nErro: o número de casos de teste deve ser maior do que zero\n")
          
        for _ in range (N):
            X, Y = map(int, (input("\nDigite os valores de X e Y (separados por espaço): \n").split()))
            if X > Y:
                X, Y = Y, X
            soma = sum(i for i in range(X + 1, Y) if i % 2 !=0)
            print(f"\nSoma dos números ímpares do intervalo: {soma}\n")
    except ValueError:
        print(f"\nErro: você deve digitar números inteiros!\n")
somaImpares()

print("\nSoma de Ímpares consecutivos II\n")

def somaImpares():
    print("Digite o número de casos de teste: ")
    numeroCasos = int(input())
    contador = 1
    listaCasos = []
    while 0 < contador <= numeroCasos:
        print(f"\nDigite os dois números inteiros do caso de teste {contador} (separados por espaço): \n")
        X, Y = map(int, input().split())
        listaCasos.append((X, Y))     
        contador += 1
    soma_impares = sum(num for X, Y in listaCasos for num in (X, Y) if num % 2 != 0)
    print(f"\nA soma de todos os números ímpares é: {soma_impares}\n")
somaImpares()

#Exercício 4.4

print("\nDividindo X por Y\n")

def dividindo():
    print("\nDigite a quantidade de pares de valores inteiros (X, Y): \n")
    numeroPares = int(input())
    contador = 1
    listaPares = []
    while 0 < contador <= numeroPares:
        print(f"\nDigite os dois números inteiros do par (X, Y) {contador} (separados por espaço): \n")
        X, Y = map(int, input().split())
        listaPares.append((X, Y))     
        contador += 1
    for X, Y in listaPares:
        if Y != 0:
            resultado = X / Y
            print(f"\nO resultado da divisão de {X} por {Y} é: {resultado:.1f}\n")
        else:
            print(f"\nA divisão de {X} por {Y} é impossível!\n")
dividindo()

#Exercício 4.5.

print("\nResto da divisão\n")

def restoDiv():
    listaNumeros = []
    while True:
        try:
            print("\nDigite dois números inteiros e positivos (separados por espaço): \n")
            X, Y = map(int, input().split())
            listaNumeros.append((X, Y))
        
            if X > 0 and Y > 0:
                break  
            else:
                print("\nDigite valores inteiros e positivos. Tente novamente.\n")
        except ValueError:
            print("\nEntrada inválida! Digite números inteiros.\n")
    
    print("\nValores cujo resto da divisão por 5 é igual a 2 ou 3: \n")
    for num in range(X, Y):
        if num % 5 == 2 or num % 5 == 3:
            print(f"\n{num}\n")
restoDiv()
