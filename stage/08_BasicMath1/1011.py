import sys

T = int(sys.stdin.readline())

for _ in range(T):
    x, y = map(int, sys.stdin.readline().split())
    d = y - x
    n = 1
    while True:
        start = n ** 2
        end = (n + 1) ** 2 - 1
        if start <= d <= end:
            result = 1 + 2 * (n - 1)
            chk1 = start + 1
            chk2 = chk1 + n
            if d < chk1: pass
            elif d < chk2: result += 1
            else: result += 2
            print(result)
            break
        n += 1