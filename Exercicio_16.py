num = int(input("Informe um número inteiro positivo ímpar: \n"))

if num % 2 != 0:
    print("Os números ímpares do número escolhido até 1 são: ")
    for i in range(num, -1, -1):
        if i % 2 != 0:
            print(i, end=" ")

else:
    print("Não é um número inteiro ímpar.")
