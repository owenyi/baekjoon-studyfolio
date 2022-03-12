V = int(input())
E = int(input())
START = 1

def dfs():
    stack = [START]

    while stack:
        now = stack.pop()
        if visited[now]:
            continue
        visited[now] = True
        for next in graph[now]:
            stack.append(next)

visited = [False] * (V  + 1)

graph = [[] for _ in range(V + 1)]

for _ in range(E):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs()
print(sum(visited) - 1)