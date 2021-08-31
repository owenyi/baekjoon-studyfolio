import sys

N = 9999
isPrime = [False, False] + [True] * (N - 1)
for i in range(2, int(N**.5) + 1):
    for j in range(i * 2, N + 1, i):
        if isPrime[j]: isPrime[j] = False

T = int(sys.stdin.readline())
for _ in range(T):
    n = int(sys.stdin.readline())
    if n == 4: # 혼자 예외인 경우(2짝수, 2짝수)
        print(2, 2)
        continue
    start = int(n // 2)
    if start % 2 == 0: start -= 1
    for i in range(start, 2, -2):
        if isPrime[i] and isPrime[n - i]:
            print(i, n - i)
            break