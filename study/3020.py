N, H = map(int, input().split())

down = [0] * (H + 1)  # 석순
up = [0] * (H + 1)  # 종유석

for i in range(N):
    if i % 2 == 0:
        down[int(input())] += 1
    else:
        up[int(input())] += 1

for i in range(H - 1, 0, -1):
    down[i] += down[i + 1]
    up[i] += up[i + 1]

count = 1
_min = N
for i in range(1, H + 1):
    cur = down[i] + up[H + 1 - i]
    if cur < _min:
        _min = cur
        count = 1
    elif cur == _min:
        count += 1
print(_min, count)