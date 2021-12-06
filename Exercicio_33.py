print("Informe dois números ('i' e 'j') e a quantidade de múltiplos ('n') que seja obter relativo a 'i' e/ou 'j': ")
i = int(input("i: "))
j = int(input("j: "))
n = int(input("n: "))
qt = 0
qt2 = 0

while qt != n:
    if qt2 % j == 0 or qt2 % i == 0:
        print(qt2, end='  ')
        qt += 1
    qt2 += 1
