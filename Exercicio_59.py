maior = -9999999
menor = 9999999
soma = 0
consumo_1 = 0
consumo_2 = 0
consumo_3 = 0

print("*" * 34)
print("RELATÓRIO DO CONSUMO DE HABITANTES")
print("*" * 34)
num_hab = int(input("\nInsira quantos habitantes a cidade possui: "))
kwh = float(input("Insira o valor do kWh: R$ "))

for h in range(1, num_hab + 1):
    consumo = float(input(f"\nInsira quantos kWh o habitante {h} consumiu este mês: "))
    codigo = int(input(f"Insira o código do habitante {h} de acordo com a relação abaixo."
                       f" \n(1 - Residencial / 2 - Comercial / 3 - Industrial): "))
    if consumo > maior:
        maior = consumo
    if consumo < menor:
        menor = consumo
    if codigo == 1:
        consumo_1 += consumo
    elif codigo == 2:
        consumo_2 += consumo
    elif codigo == 3:
        consumo_3 += consumo

    soma += consumo

print(f"\nO maior consumo entre os habitantes foi {maior} kWh.")
print(f"O menor consumo entre os habitantes foi {menor} kWh.")
print(f"A média de consumo entre os habitantes foi de {soma/num_hab} kWh.")
print(f"O total do consumo de habitantes da categoria 1 foi de {consumo_1} kwh.")
print(f"O total do consumo de habitantes da categoria 2 foi de {consumo_2} kwh.")
print(f"O total do consumo de habitantes da categoria 3 foi de {consumo_3} kwh.")
