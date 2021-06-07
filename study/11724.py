def dfs(v):
    if visited[v]: return 0
    visited[v] = True
    for next in graph[v]:
        if not visited[next]: dfs(next)
    return 1

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for x in range(1, N + 1):
    cnt += dfs(x)
print(cnt)