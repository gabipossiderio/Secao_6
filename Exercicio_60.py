soma = 0
num = 1
qtd_num = -1
maior = -9999999
menor = 9999999
pares = 0
qtd_pares = 0

print("Informe quantos números quiser. Para sair, digite 0: ")

while num != 0:
    num = float(input())
    soma += num
    qtd_num += 1
    if num != 0:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
        if num % 2 == 0:
            pares += num
            qtd_pares += 1

print(f"A) A soma dos números digitados é {soma}.")
print(f"B) Você digitou {qtd_num} números válidos.")
print(f"C) A média dos números digitados é {soma/qtd_num}.")
print(f"D) O maior número digitado é {maior}.")
print(f"E) O menor número digitado é: {menor}.")
print(f"F) A média dos números pares é {pares/qtd_pares}.")
