from itertools import permutations

N, M = map(int, input().split()) # 4 2
perm_list = list(permutations([i for i in range(1, N + 1)], M))
for perm in perm_list:
    for p in perm:
        print(p, end=' ')
    print()