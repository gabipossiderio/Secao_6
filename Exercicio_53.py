n = int(input("Insira a quantidade de linhas que deseja imprimir no Triângulo de Floyd: "))
num = 1
for linha in range(1, n + 1):
    for quantidade_de_numeros_na_linha in range(1, linha + 1):
        print(num, end=" ")
        num += 1
    print()
