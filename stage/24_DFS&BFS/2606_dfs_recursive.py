V = int(input())
E = int(input())
START = 1

def dfs(now):
    if visited[now]:
        return
    visited[now] = True
    for next in graph[now]:
        dfs(next)

visited = [False] * (V  + 1)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(START)
print(sum(visited) - 1)