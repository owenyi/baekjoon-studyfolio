import sys
input = sys.stdin.readline

from collections import Counter

def check(n, broken):
    while True:
        if broken[n % 10] == 1: return False
        n //= 10
        if n == 0: break
    return True

N = int(input())
M = int(input())
broken = Counter(map(int, input().split()))
answer = abs(N - 100)
for i in range(1000001):
    if check(i, broken):
        new = abs(N - i) + len(str(i))
        if new < answer: answer = new
print(answer)