maior = -999999
menor = 9999999
num = 1

print("Digite quantos números quiser. Retornaremos o maior e o menor número lido. Para encerrar, digite um número "
      "negativo: \n")

while num >= 0:
    num = int(input())
    if num > maior:
        maior = num
    if 0 <= num < menor:
        menor = num
    if num < 0:
        print("\nVocê encerrou o programa. Faremos o cálculo para você.")

print(f"\nO maior número digitado é {maior} e o menor número digitado é {menor}.")
