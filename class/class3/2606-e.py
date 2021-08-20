# BFS

n = int(input())
graph = [[] for _ in range(n + 1)]
for _ in range(int(input())):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

from collections import deque
visited = [False] * (n + 1)
queue = deque([1])
while queue:
    now = queue.popleft()
    visited[now] = True
    for next in graph[now]:
        if visited[next] == False: queue.append(next)

print(sum(visited) - 1)