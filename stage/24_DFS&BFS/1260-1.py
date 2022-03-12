V, E, start = map(int, input().split())
graph = [[] for _ in range(V + 1)]
for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, V + 1):
    graph[i].sort()

def dfs():
    visited = [False] * (V + 1)

    stack = [start]

    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        print(now, end=' ')
        visited[now] = True
        for next in graph[now][::-1]:
            stack.append(next)

def bfs():
    visited = [False] * (V + 1)

    queue = [start]
    visited[start] = True

    while queue: # queue가 있는 동안에 <-> queue가 비면 종료
        now = queue.pop(0)
        print(now, end=' ')
        for next in graph[now]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = True

dfs()
print()
bfs()