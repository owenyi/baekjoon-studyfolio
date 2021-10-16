import sys

sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def union(v1, v2):
    p1, p2 = find(v1), find(v2)
    if p1 == p2: return
    parent[p1] = p2

def find(v):
    if parent[v] == -1: return v
    parent[v] = find(parent[v])
    return parent[v]

N, M = map(int, input().split())

parent = [-1] * (N + 1)

for _ in range(M):
    command, a, b = map(int, input().split())
    if command == 1:
        if find(a) == find(b):
            sys.stdout.write("YES\n")
        else:
            sys.stdout.write("NO\n")
    elif command == 0:
        union(a, b)