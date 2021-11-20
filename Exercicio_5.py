print("Digite 10 números. Iremos somá-los para você.\n".upper())

soma = 0

for num in range(0, 10):
    num1 = float(input("Número escolhido: "))
    soma += num1

print(f"\nA soma dos números escolhidos é: {soma}.")
