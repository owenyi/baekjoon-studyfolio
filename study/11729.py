def hanoi(n, a, b, c):
    if n == 1: tap.append(str(a) + ' ' + str(c))
    else:
        hanoi(n - 1, a, c, b)
        tap.append(str(a) + ' ' + str(c))
        hanoi(n - 1, b, a, c)

tap = []
hanoi(int(input()), 1, 2, 3)
print(len(tap))
for x in tap: print(x)