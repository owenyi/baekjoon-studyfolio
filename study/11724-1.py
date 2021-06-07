# bfs

from collections import deque

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)
for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

cnt = 0
for x in range(1, N + 1):
    if visited[x]: continue
    cnt += 1
    queue = deque([x])
    visited[x] = True
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if not visited[next]:
                queue.append(next)
                visited[next] = True
print(cnt)