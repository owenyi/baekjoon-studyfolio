from math import sqrt

M, N = map(int, input().split())

def isPrime(x):
    if x == 1: return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0: return False
    return True

for i in range(M, N + 1):
    if isPrime(i):
        print(i)