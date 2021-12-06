print("*" * 10)
print("BANCO GABI")
print("*" * 10)
saque = int(input("\nSeja bem-vindo (a). Insira o valor do saque: R$ "))
cedula = 100
total_cedulas = 0

while True:
    if saque >= cedula:
        saque -= cedula
        total_cedulas += 1
    else:
        if total_cedulas > 0:
            print(f"\nVocê sacará {total_cedulas} cédulas de R${cedula}.")
        if cedula == 100:
            cedula = 50
        elif cedula == 50:
            cedula = 20
        elif cedula == 20:
            cedula = 10
        elif cedula == 10:
            cedula = 5
        elif cedula == 5:
            cedula = 2
        elif cedula == 2:
            cedula = 1
        total_cedulas = 0
        if saque == 0:
            break



