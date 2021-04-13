def cal(x):
    digits = list(map(int, str(x)))
    return x + sum(digits)

def sol(n):
    for M in range(max(1, N - 54), N):
        if cal(M) == N:
            return M
    return 0

N = int(input())

print(sol(N))