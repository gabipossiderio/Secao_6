print("Digite o valor final e o valor final do intervalo, respectivamente:")
valor_inicial = int(input())
valor_final = int(input())
soma = 0

if valor_final > valor_inicial:
    for i in range(valor_inicial, valor_final + 1):
        if i % 2 != 0:
            soma += i
else:
    print("Intervalo de valores inválido.")

print(f"A soma dos números ímpares no intervalo é {soma}")
