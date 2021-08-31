import sys

N = 123456 * 2
isPrime = [False, False] + [True] * (N - 1)
for i in range(2, int(N**.5) + 1):
    for j in range(i * 2, N + 1, i):
        if isPrime[j]: isPrime[j] = False

while True:
    n = int(sys.stdin.readline())
    if n == 0: break
    print(sum(isPrime[n + 1:2*n + 1]))
