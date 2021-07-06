def find_parent(parent, x):
    if parent[x] == x: return x
    return find_parent(parent, parent[x])

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b: parent[b] = a
    else: parent[a] = b

N = int(input())
M = int(input())
parent = [i for i in range(N + 1)]
for i in range(1, N + 1):
    row = input().split()
    for j in range(1, N + 1):
        if row[j - 1] == '1': union_parent(parent, i, j)

tour = list(map(int, input().split()))
tour_1st = find_parent(parent, tour[0])
flag = True
for x in tour[1:]:
    if tour_1st != find_parent(parent, x): flag = False
if flag: print("YES")
else: print("NO")