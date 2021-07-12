def find_parent(x):
    if parent[x] == x: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort(reverse=True)

c, d = map(int, input().split())
for cost, a, b in edges:
    union_parent(a, b)
    result += cost
    if find_parent(c) == find_parent(d):
        print(cost)
        break