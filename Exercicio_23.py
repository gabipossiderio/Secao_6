num = int(input("Insira um número inteiro. Retornaremos os divisores dele pra você: "))

for i in range(1, num + 1):
    if num % i == 0:
        print(i)
