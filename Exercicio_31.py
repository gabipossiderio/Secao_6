numerador = range(1, 100, 2)
denominador = range(1, 51)
soma = 0

for i in range(50):
    soma += numerador[i] / denominador[i]

print(soma)
