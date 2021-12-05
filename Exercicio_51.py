ano = 1996
aumento = 0.015
salario = 2030

while ano != 2021:
    ano += 1
    aumento *= 2
    salario = salario + (salario * aumento)

print(f"Seu salário atual é {salario}.")
