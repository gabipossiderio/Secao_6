idade = 1
soma = 0
qtd_pessoas = 0

print("Informe a idade de cada componente do grupo. Para sair, digite 0: ")

while idade != 0:
    idade = float(input())

    if idade != 0:
        qtd_pessoas += 1
        soma += idade

print(f"A média de idade desse grupo é {soma/qtd_pessoas}.")
