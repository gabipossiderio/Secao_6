from random import randint

num = (randint(1, 1000))
chute = 0
qtd_tentativas = 0

print("Acabei de imaginar um número de 1 a 1000. Vamos tentar adivinhar?")

while chute != num:
    chute = int(input("\nChute um número inteiro: "))
    qtd_tentativas += 1
    if chute > num:
        print("\nQue pena. Você errou! Esse número é maior do que o número certo.")
    if chute < num:
        print("\nQue pena. Você errou! Esse número é menor do que o número certo.")

print(f"\nParabéns! Você acertou em {qtd_tentativas} tentativas.")
