def find_parent(x):
    if parent[x] == x: return x
    return find_parent(parent[x])

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]

degrees = [-1]
degrees += list(map(int, input().split()))

edges = []
for _ in range(e):
    a, b, cost = map(int, input().split())
    edges.append((cost, a, b))

counts = [0] * (v + 1)
check = [False] * e
path =[]
result = []
max_sum = 1000000000
def makeResult(start, _sum, cnt):
    if cnt == v - 1:
        global result, max_sum
        if max_sum > _sum:
            result = path.copy()
            max_sum = _sum
            return
    for i in range(start, e):
        if check[i]: continue
        cost, a, b = edges[i]
        pa, pb = find_parent(a), find_parent(b)
        if pa != pb and counts[a] < degrees[a] and counts[b] < degrees[b]:
            if pa > pb: pa, pb = pb, pa
            ppb = parent[pb]
            parent[pb] = pa
            check[i] = True
            counts[a] += 1
            counts[b] += 1
            path.append((a, b))

            makeResult(i, _sum + cost, cnt + 1)

            parent[pb] = ppb
            check[i] = False
            counts[a] -= 1
            counts[b] -= 1
            del path[-1]

makeResult(0, 0, 0)
if v == 1:
    print("YES")
elif result:
    print("YES")
    for v1, v2 in result:
        if v1 > v2: v1, v2 = v2, v1
        print(v1, v2)
else: print("NO")