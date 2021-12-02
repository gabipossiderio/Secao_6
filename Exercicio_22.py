num_dados = 0
num = 10
soma = 0

print("\nInforme uma sequência de notas (válidas no intervalo de 10 a 20). Para finalizar, digite 100: ")

while 10 <= num <= 20:

    num = float(input())

    if 10 <= num <= 20:
        num_dados += 1
        soma += num

print(f"A sua média aritmética é {soma/num_dados}."
      f" Programa finalizado. Caso ainda não tenha terminado, volte ao início e insira notas válidas.")
