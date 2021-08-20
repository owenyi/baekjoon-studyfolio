from math import sqrt

def isPrime(x):
    if x == 1: return False
    for i in range(2, int(sqrt(x)) + 1):
        if x % i == 0: return False
    return True

N = int(input())
nums = list(map(int, input().split()))
cnt = 0
for x in nums:
    if isPrime(x): cnt += 1
print(cnt)