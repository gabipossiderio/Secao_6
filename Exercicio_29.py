fatorial = 1
soma = 0

for i in range(2, 6):
    fatorial *= i
    soma += 1 / fatorial

print(soma)
