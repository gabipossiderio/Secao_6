print("Digite 10 números inteiros positivos. Iremos descobrir a média deles para você.\n".upper())

soma = 0
counter = 0

for num in range(0, 10):
    num1 = int(input("Número escolhido: "))
    if num1 >= 0:
        counter += 1
        soma += num1

print(f"\nA média dos {counter} números positivos é: {soma / counter}.")
