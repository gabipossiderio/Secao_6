opcao = 0
num1 = float(input("Insira o primeiro número para o cálculo: "))
num2 = float(input("Insira o segundo número para o cálculo: "))

while opcao != 5:
    opcao = int(input("""
    \nMENU DE OPÇÕES\n
    Adição - Digite 1
    Subtração - Digite 2
    Multiplicação - Digite 3
    Divisão - Digite 4
    Saída - Digite 5\n
    Opção escolhida:
    """))
    match opcao:
        case 1:
            print(f"\nA soma dos dois números digitados é igual a {num1+num2}.")
        case 2:
            print(f"\nA subtração dos dois números digitados é igual a {num1-num2}.")
        case 3:
            print(f"\nA multiplicação dos dois números digitados é igual a {num1*num2}.")
        case 4:
            print(f"\nA divisão dos dois números digitados é igual a {num1/num2}.")
        case 5:
            print("\nVocê saiu do menu. Volte sempre!")
        case _:
            print("\nOpção inválida!")
