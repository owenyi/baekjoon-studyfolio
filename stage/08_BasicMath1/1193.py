import sys

X = int(sys.stdin.readline())

n = 1
while True:
    start = 1 + n * (n - 1) // 2
    end = (n + 1) * n // 2
    if start <= X <= end:
        m = X - start
        if n % 2 == 0:
            print(f"{(1 + m)}/{(n - m)}")
        else:
            print(f"{(n - m)}/{(1 + m)}")
        break
    n += 1