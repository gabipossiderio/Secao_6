num = int(input("Informe um número inteiro positivo. Iremos somá-los para você: "))
soma = 0

if num > 0:
    for num in range(num):
        soma += num

else:
    print("Não é um número inteiro positivo! Tente novamente.")

print(f"A soma dos {num} primeiros números é {soma}.")
