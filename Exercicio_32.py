from random import randint

n = int(input("Informe quantas vezes os dados serão lançados:"))

d1 = 0
d2 = 0

for i in range(n + 1):
    d1 = randint(1, 6)
    d2 = randint(1, 6)

    print(f'\nLançamento {i + 1}:')

    if d1 > d2:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 > Dado 2')

    elif d1 < d2:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 < Dado 2')

    else:
        print(f'Dado 1: {d1}')
        print(f'Dado 2: {d2}')
        print(f'Dado 1 = Dado 2')
