num = int(input("Informe um número inteiro positivo ímpar: \n"))

if num % 2 != 0:
    print("Os números ímpares de 1 até o número escolhido são: ")
    for i in range(1, num + 1):
        if i % 2 != 0:
            print(i, end=" ")

else:
    print("Não é um número inteiro ímpar.")
