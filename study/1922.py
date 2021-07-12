def find_parent(x):
    if parent[x] == x: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

v = int(input())
e = int(input())
parent = [i for i in range(v + 1)]

edges = []
result = 0

for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

edges.sort()

for cost, a, b in edges:
    if find_parent(a) != find_parent(b):
        union_parent(a, b)
        result += cost

print(result)