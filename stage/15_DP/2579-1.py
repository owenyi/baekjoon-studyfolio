N = int(input())
memos = [[0, 0], [0, 0]]

for i in range(N):
    step = int(input())
    memos.append([step + memos[i + 1][1], step + max(memos[i])])

print(max(memos[-1]))