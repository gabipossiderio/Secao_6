num = int(input("Digite um número inteiro maior do que 1. Verificaremos se é um número primo: "))

if num > 1:
    for i in range(2, num):
        if (num % i) == 0:
            print("O número", num, "não é um número primo.")
            break
    else:
        print("O número", num, "é um número primo.")

else:
    print("O número", num, "não é um número válido.")
