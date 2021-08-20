from itertools import permutations

N, M = map(int, input().split())
nums = list(map(int, input().split()))

perms = list(permutations(nums, 3))

max = 0
for p in perms:
    s = sum(p)
    if s > max and s <= M: max = s
print(max)