def find_parent(x):
    if x == 51: return 51
    if parent[x] == x: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(nodes):
    _min = 51
    for v in nodes:
        parent_i = find_parent(v)
        if _min > parent_i: _min = parent_i
    party.append(_min)
    for v in nodes:
        parent[parent[v]] = _min

N, M = map(int, input().split())
parent = [i for i in range(N + 1)]
party = []
witness = list(map(int, input().split()[1:]))
for _ in range(M):
    union_parent(list(map(int, input().split()[1:])))

for i in range(len(witness)):
    witness[i] = find_parent(witness[i])

cnt = 0
for p in party:
    if find_parent(p) not in witness:
        cnt += 1
print(cnt)