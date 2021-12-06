raiz = 0
digito_1_e_2 = 0
digito_3_e_4 = 0

for i in range(1_000, 10_000):
    raiz = i ** 0.5
    digito_1_e_2 = i // 100
    digito_3_e_4 = i % 100

    if digito_1_e_2 + digito_3_e_4 == raiz:
        print(i)
