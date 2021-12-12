r1 = 1
r2 = 1

while True:
    print("Informe os valores das duas resistências em ohms. Digite 0 para encerrar:")
    r1 = float(input())
    if r1 == 0:
        break
    r2 = float(input())
    if r2 == 0:
        break
    paralelo = (r1 * r2) / (r1 + r2)
    print(f"O paralelo das duas resitências informadas é {paralelo}\n")
