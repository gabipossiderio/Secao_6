print("Digite 10 números. Iremos descobrir a média deles para você.\n".upper())

soma = 0

for num in range(0, 10):
    num1 = float(input("Número escolhido: "))
    soma += num1 / 10

print(f"\nA média dos números escolhidos é: {soma}.")
