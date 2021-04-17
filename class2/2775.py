T = int(input())
for _ in range(T):
    k, n = int(input()), int(input())
    f = [[i for i in range(n + 1)]] # 0층
    for i in range(1, k + 1): # 1층 ~ k층
        f.append([1 for _ in range(n + 1)])
    for i in range(1, k + 1):
        for j in range(2, n + 1):
            f[i][j] = f[i - 1][j] + f[i][j - 1]
    print(f[k][n])