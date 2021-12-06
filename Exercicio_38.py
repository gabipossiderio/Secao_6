# a + b + c == 1000
# c² = a² + b²
a = 0
b = 0
c = 0

for a in range(1, 1001):
    for b in range(1, 1001):
        c = (a ** 2 + b ** 2) ** 0.5
        if a + b + c == 1000:
            print(a, b, int(c))
            break
    if a + b + c == 1000:
        break
