num = int(input("Informe um número inteiro positivo par: \n"))

if num % 2 == 0:
    print("Os números pares do número escolhido até 0 são: ")
    for i in range(num, -1, -1):
        if i % 2 == 0:
            print(i, end=" ")

else:
    print("Não é um número inteiro par.")
