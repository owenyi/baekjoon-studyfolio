N = int(input())
memo = [[0, 0], [0, 0]]
for _ in range(N):
    _input = int(input())
    memo.append([memo[-1][1] + _input, max(memo[-2]) + _input])
print(max(memo[-1]))