i = 1

while True:
    if i % 2 == 0 and i % 3 == 0 and i % 5 == 0 and i % 7 == 0\
            and i % 11 == 0 and i % 13 == 0 and i % 17 == 0 and i % 19 == 0:

        print(i)
        break
    else:
        i += 1
