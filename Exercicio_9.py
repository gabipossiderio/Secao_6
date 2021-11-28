num = int(input("Escolha a quantidade de números ímpares que deseja imprimir: \n"))

for i in range(1, 2 * num, 2):
    print(i, end=" ")
