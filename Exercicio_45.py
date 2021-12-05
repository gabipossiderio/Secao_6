opcao = 1
num1 = float(input("Insira a velocidade para conversão: "))

while opcao != 0:
    opcao = int(input("""
    \nMENU DE OPÇÕES\n
    Converter de KM/h para M/s - Digite 1
    Converter de M/s para KM/h - Digite 2
    Sair do MENU - Digite 0\n
    Opção escolhida:
    """))
    match opcao:
        case 1:
            print(f"\nVelocidade convertida para metros por segundo: {num1/3.6}.")
        case 2:
            print(f"\nVelocidade convertida para quilômetros por hora: {num1*3.6}.")
        case 0:
            print("\nVocê saiu do menu. Volte sempre!")
        case _:
            print("\nOpção inválida!")
