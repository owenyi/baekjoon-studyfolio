N = int(input())
memo = [0, 0]
for i in range(2, N + 1):
    _min = memo[i - 1]
    if i % 2 == 0: _min = min(_min, memo[i // 2])
    if i % 3 == 0: _min = min(_min, memo[i // 3])
    memo.append(_min + 1)
print(memo[-1])