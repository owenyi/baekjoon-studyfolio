S = [0] * 1001

L = int(input())

for s in input().split():
    S[int(s)] = 1

n = int(input())

if S[n]: print(0)
else:
    infimum = 0
    for i in range(n + 1, 1001):
        if S[i]:
            supremum = i # 상한
            break
    for i in range(n - 1, 0, -1):
        if S[i]:
            infimum = i # 하한
            break
    print((supremum - n) * (n - infimum) - 1)