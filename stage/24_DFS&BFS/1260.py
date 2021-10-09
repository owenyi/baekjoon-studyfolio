def dfs(now):
    dfs_visited[now] = True
    print(now, end=' ')
    for next in links[now]:
        if not dfs_visited[next]:
            dfs(next)

def bfs(start):
    bfs_visited[start] = True
    queue = [start]
    while queue:
        now = queue.pop(0)
        print(now, end=' ')
        for next in links[now]:
            if not bfs_visited[next]:
                queue.append(next)
                bfs_visited[next] = True

V, E, start = map(int, input().split())

links = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    links[a].append(b)
    links[b].append(a)
for link in links:
    link.sort()

dfs_visited = [False] * (V + 1)
bfs_visited = [False] * (V + 1)
dfs(start)
print()
bfs(start)