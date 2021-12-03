n = int(input("Informe um número, será retornado o valor de H(n) (função harmônica): "))
soma = 0

for i in range(1, n + 1):
    soma += 1 / i

print(soma)