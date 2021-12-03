soma = 0

for i in range(1001):
    if i % 3 == 0 or i % 5 == 0:
        soma += i

print(f"A soma dos números múltiplos de 3 e 5 e que estão entre 0 e 1000 é {soma}.")
