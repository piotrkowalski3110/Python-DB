def Fibbo(start, end):
    a, b, n = 0, 1, 0
    while True:
        if n in range(start, end+1):
                yield a
        if n > end:
            break
        else:
            a, b = b, a + b
            n += 1


for i in Fibbo(7, 9):
    print(i)
