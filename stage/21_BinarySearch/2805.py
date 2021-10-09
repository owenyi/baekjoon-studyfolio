N, key = map(int, input().split())
targets = list(map(int, input().split()))
# targets.sort() # 정렬 할 필요 없음

bot, top = 0, max(targets)
while bot <= top:
    mid = (bot + top) // 2
    sum_cut = 0
    for target in targets:
        sum_cut += max(target - mid, 0)
    if sum_cut < key: top = mid - 1
    else: bot = bot = mid + 1
print(top)