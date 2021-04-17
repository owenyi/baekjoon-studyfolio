N, M = map(int, input().split())
lenList = list(map(int, input().split()))

bot = 1
top = max(lenList)
while bot <= top:
    mid = (bot + top) // 2
    s = 0
    for x in lenList:
        sub = x - mid
        if sub > 0: s += sub
    if s >= M: # 높이를 높여야 함
        bot = mid + 1
    elif s < M:
        top = mid - 1
print(top)