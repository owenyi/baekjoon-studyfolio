from itertools import combinations

N, M = map(int, input().split())
comb_list = list(combinations([i for i in range(1, N + 1)], M))
for comb in comb_list:
    for c in comb:
        print(c, end=' ')
    print()