n = int(input("Informe um número inteiro positivo N, será retornado o valor da operação 1 + 1/2! + ... + 1/N!: "))
fatorial = 1
soma = 0

for i in range(1, n + 1):
    fatorial *= i
    soma += 1 / fatorial

print(soma)
