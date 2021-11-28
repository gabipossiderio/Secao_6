print("Digite 10 números. Iremos descobrir o menor e o maior deles para você.\n")

maior = -999
menor = 999

for i in range(0, 10):
    num = int(input(f"Número escolhido ({i}/10): "))
    if num > maior:
        maior = num
    if num < menor:
        menor = num

print(f"\nO maior número digitado é {maior} e o menor número digitado é: {menor}.")
