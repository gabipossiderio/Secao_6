soma_dos_quadrados = 0
soma = 0

for i in range(101):
    soma_dos_quadrados += i ** 2
    soma += i

print(f"A diferença do quadrado da soma dos números pela soma dos quadrados é {soma ** 2 - soma_dos_quadrados}")
