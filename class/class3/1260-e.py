def DFS(link, visited, start):
    print(start, end=' ')
    visited[start] = True
    for x in link[start]:
        if visited[x] == False: DFS(link, visited, x)

from collections import deque
def BFS(link, visited, start):
    queue = deque([start])
    while queue:
        now = queue.popleft()
        visited[now] = True
        print(now, end=' ')
        for x in link[now]:
            if visited[x] == False: queue.append(x)

N, M, V = map(int, input().split())
visited1 = [False] * (N + 1)
visited2 = [False] * (N + 1)
link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
for x in link: x.sort()
DFS(link, visited1, V)
print()
BFS(link, visited2, V)