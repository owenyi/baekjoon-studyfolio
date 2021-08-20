# DFS recursion

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
def dfs(v):
    visited[v] = True
    for next in graph[v]:
        if visited[next] == False: dfs(next)

dfs(1)
print(sum(visited) - 1)