V = int(input())
E = int(input())
START = 1

def bfs():
    queue = [START]
    visited[START] = True

    while queue:
        now = queue.pop(0)
        for next in graph[now]:
            if visited[next]:
                continue
            queue.append(next)
            visited[next] = True

visited = [False] * (V  + 1)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

bfs()
print(sum(visited) - 1)