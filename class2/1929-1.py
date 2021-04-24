# 에라토스테네스의 체

from math import sqrt, ceil

M, N = map(int, input().split())
primes = [True] * (N + 1)
primes[1] = False
for i in range(2, int(sqrt(N)) + 1):
    if primes[i]:
        for j in range(i, ceil(N // i) + 1):
            if primes[i * j] == False: continue
            else: primes[i * j] = False
for i in range(M, N + 1):
    if primes[i]: print(i)