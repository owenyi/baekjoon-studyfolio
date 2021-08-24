N = int(input())
steps = [int(input()) for _ in range(N)]

memos = [[0, 0], [0, 0]]
for i, now in enumerate(steps):
    memos.append([now + memos[i+1][1], now + max(memos[i])])

print(max(memos[-1]))