num = int(input("Insira um número inteiro. Retornaremos a soma dos divisores dele pra você: "))
soma = 0

for i in range(1, num):
    if num % i == 0:
        soma += i

print(soma)
