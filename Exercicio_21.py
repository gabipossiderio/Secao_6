print("Digite dois números para que o um cálculo seja feito.\n")
num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
soma = 0
multiplicacao = 1

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        soma += i

    else:
        multiplicacao *= i

print(f"\nOs números pares desse intervalo de números somado aos dois números digitados é igual a {soma}.\nOs números "
      f"ímpares desse intervalo de números multiplicados com os dois números digitados é igual a {multiplicacao}.")
