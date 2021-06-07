# combinations 직접 구현

def combinations(n, m):
    check = [0] * (n + 1)
    comb_list = []
    comb = []
    def combination(start):
        if len(comb) == m:
            comb_list.append(comb.copy())
            return
        for i in range(start, n + 1):
            if check[i] == 1: continue
            check[i] = 1
            comb.append(i)
            combination(i)
            check[i] = 0
            del comb[-1]
    combination(1)
    return comb_list

N, M = map(int, input().split())
comb_list = combinations(N, M)
for comb in comb_list:
    for c in comb:
        print(c, end=' ')
    print()