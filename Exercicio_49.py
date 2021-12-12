carlos = 300
joao = 300 / 3
qtd_meses = 0

while joao < carlos:
    carlos = carlos + (carlos * 0.02)
    joao = joao + (joao * 0.05)
    qtd_meses += 1

print(f"João precisou de {qtd_meses} meses para alcançar o valor de Carlos.")
