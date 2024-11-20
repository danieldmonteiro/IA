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