num = input("Insira um número inteiro entre 100 e 999: ")

if 100 <= int(num) <= 999:
    for i in range(3):
        print(num[i])

else:
    print("Número inválido. Tente novamente!")
