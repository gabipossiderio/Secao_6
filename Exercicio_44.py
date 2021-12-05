num1 = int(input("Insira um número. Retornaremos a sequência Fibonacci até o primeiro número superior a ele: "))
num2 = 0
num3 = 1
print(num2)
print(num3)
while num3 < num1:
    num2_provisorio = num3
    num3 = num2 + num3
    num2 = num2_provisorio
    print(num3)