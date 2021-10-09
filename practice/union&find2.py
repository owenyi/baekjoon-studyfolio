def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    if p1 == p2: return
    parent[p1] = p2

def find(v):
    # if parent[v] == -1: return v # -1인 경우에 같은 집합임을 확인할 수 없음
    if parent[v] == v: return v # return 아니고 return v!!
    parent[v] = find(parent[v])
    return parent[v]

N, M = map(int, input().split())

# parent = [-1] * (N + 1) # -1인 경우에 같은 집합임을 확인할 수 없음
parent = [i for i in range(N + 1)]

for _ in range(M):
    command, a, b = map(int, input().split())
    if command == 1:
        if find(a) == find(b):
            print("YES")
        else:
            print("NO")
    elif command == 0:
        union(a, b)