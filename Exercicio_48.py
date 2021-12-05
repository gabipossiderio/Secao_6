num2 = 0
num3 = 1
soma = 0

while num3 + num2 < 4000000:
    num2_provisorio = num3
    num3 = num2 + num3
    num2 = num2_provisorio
    if num3 % 2 == 0 and num3 < 4000000:
        soma += num3

print(f"A soma dos termos de valor par da sequência Fibonacci é {soma}.")
