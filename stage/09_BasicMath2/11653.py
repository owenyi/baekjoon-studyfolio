import sys


def solution(n):
    if n == 1: return

    primes = [False, False] + [True] * (n - 1)
    for i in range(2, n + 1):
        if not primes[i]: continue
        for j in range(i * 2, n + 1, i):
            if primes[j]: primes[j] = False

    result = []
    i = 2
    while i <= n:
        if primes[n]:
            result.append(n)
            break
        if primes[i] and n % i == 0:
            n //= i
            result.append(i)
        else:
            i += 1
    for x in result:
        print(x)


N = int(sys.stdin.readline())
solution(N)