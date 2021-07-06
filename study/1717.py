import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(x):
    if parent[x] == x: return x
    parent[x] = find_parent(parent[x])
    return parent[x]

def union_parent(a, b):
    a = find_parent(a)
    b = find_parent(b)
    if a < b: parent[b] = a
    else: parent[a] = b

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for i in range(m):
    operating, a, b = map(int, input().split())
    if operating == 0: union_parent(a, b)
    elif operating == 1:
        isSibling = find_parent(a) == find_parent(b)
        if isSibling: sys.stdout.write("YES\n")
        else: sys.stdout.write("NO\n")