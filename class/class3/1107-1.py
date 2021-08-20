import sys
input = sys.stdin.readline

from collections import Counter

def check(n, broken):
    for x in str(n):
        if broken[x] == 1: return False
    return True

N = int(input())
M = int(input())
broken = Counter(input().split())
answer = abs(N - 100)
for i in range(1000001):
    if check(i, broken):
        new = abs(N - i) + len(str(i))
        if new < answer: answer = new
print(answer)