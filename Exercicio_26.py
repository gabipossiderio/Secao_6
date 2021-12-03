num = int(input("Insira um número inteiro e a partir dele encontraremos o primeiro múltiplo de 11, 13 ou 17: "))

while True:
    if num % 11 == 0 or num % 13 == 0 or num % 17 == 0:
        print(num)
        break
    num += 1
