num_dados = 0
num_pares = 0
num = 0

print("Informe uma sequência de números. Para sair, digite 1000: ")

while num != 1000:

    num = int(input())

    if num != 1000:
        num_dados += 1

    if num % 2 == 0 and num != 1000:
        num_pares += 1

if num_dados != 0:
    print(f"{num_pares} dos {num_dados} números inseridos são pares.")