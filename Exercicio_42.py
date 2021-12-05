num = 1

print("Informe quantos números quiser. Para sair, digite 0 ou um valor negativo: ")

while 0 > num or num != 0:
    num = float(input())
    print(f"O quadrado do número acima é {num ** 2}, o cubo é {num ** 3} e a raiz quadrada é {num ** 0.5}.")
