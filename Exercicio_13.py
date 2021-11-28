num = int(input("Informe um número inteiro positivo par: \n"))

if num % 2 == 0:
    print("Os números pares de 0 até o número escolhido são: ")
    for i in range(0, num + 1):
        if i % 2 == 0:
            print(i, end=" ")

else:
    print("Não é um número inteiro par.")
