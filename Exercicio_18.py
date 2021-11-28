qt_num = int(input("Insira quantos números deseja inserir: "))
qt_maior = 0
maior = -99999999

for i in range(0, qt_num):
    num = float(input(f"Número {i + 1}: "))
    if num > maior:
        maior = num
        qt_maior += 1

print(f"\nO maior número digitado é {maior}.")
print(f"\nVocê digitou um número maior que os outros {qt_maior - 1} vezes.")
