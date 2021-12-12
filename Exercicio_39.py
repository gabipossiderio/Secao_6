base = float(input("Informe o tamanho da base do triângulo: "))
altura = float(input("Infomre a altura do triângulo: "))

if base > 0 and altura > 0:
    area = (base * altura) / 2
    print(f"A area do triângulo é {area}")
else:
    print("Os dados informados devem ser maiores que 0.")
