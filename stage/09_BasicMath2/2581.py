import sys

M = int(sys.stdin.readline())
N = int(sys.stdin.readline())

primes = [True] * (N + 1)
primes[1] = False

for i in range(2, N // 2 + 1):
    if not primes[i]: continue
    j = 2
    while True:
        k = i * j
        if k > N: break
        if primes[k]: primes[k] = False
        j += 1

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