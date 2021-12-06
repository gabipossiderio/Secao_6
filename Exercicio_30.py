n = int(input("f(n) = 1 + 2 + 3 + ... + n\n"
              "g(n) = 1 - 2 + 3 - 4 + ... + (2n - 1)\n"
              "h(n) = 1 + 3 + 5 + 7 + ... + (2n - 1)\n"
              "Informe um número n para que seja realizada as operações acima: "))

resultado_f = 0
resultado_h = 0
resultado_g = 0

for i in range(n + 1):
    resultado_f += i

for i in range(1, 2 * n):
    if i % 2 != 0:
        resultado_g += i
        resultado_h += i
    else:
        resultado_g -= i

print(f"f(n) = {resultado_f}\n"
      f"g(n) = {resultado_g}\n"
      f"h(n) = {resultado_h}")
