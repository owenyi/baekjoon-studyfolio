# permutation 직접 구현

def permutations(n, m):
    check = [0] * (n + 1)
    perm_list = []
    perm = []
    def permutation():
        if len(perm) == m:
            perm_list.append(perm.copy())
            return
        for i in range(1, n + 1):
            if check[i] == 1: continue
            check[i] = 1
            perm.append(i)
            permutation()
            check[i] = 0
            del perm[-1]
    permutation()
    return perm_list

N, M = map(int, input().split())
perm_list = permutations(N, M)
for perm in perm_list:
    for p in perm:
        print(p, end=' ')
    print()