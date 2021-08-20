T = int(input())
for _ in range(T):
    H, W, N = map(int, input().split())
    h = N % H
    w = N // H + 1
    if h == 0:
        h = H
        w -= 1
    print(h * 100 + w)