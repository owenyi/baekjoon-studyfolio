import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

primes = [False, False] + [True] * (N - 1) #

for i in range(2, int(N**.5) + 1): #
    if not primes[i]: continue
    for j in range(i * 2, N + 1, i):
        if primes[j]: primes[j] = False

result1 = 0
result2 = 0
for i in range(M, N + 1):
    if primes[i]:
        if result2 == 0: result2 = i
        result1 += i

if result2:
    print(result1)
    print(result2)
else:
    print(-1)