import sys
input = sys.stdin.readline
from collections import deque

def bfs(start):
    if visited[start]: return
    visited[start] = 1
    queue = deque([start])
    while queue:
        now = queue.popleft()
        for next in graph[now]:
            if visited[next]: continue
            visited[next] = 2 - (visited[now] + 1) % 2
            queue.append(next)

def isBinary():
    global v
    for u in range(1, v + 1):
        group_u = visited[u]
        for v in graph[u]:
            if group_u == visited[v]: return False
    return True

if __name__ == "__main__":
    K = int(input())
    for _ in range(K):
        v, e = map(int, input().split())

        visited = [0] * (v + 1) # 0: 방문x, 1: 홀수depth, 2: 짝수depth

        graph = [[] for _ in range(v + 1)]
        for _ in range(e):
            a, b = map(int, input().split())
            graph[a].append(b)
            graph[b].append(a)

        start = 1
        for u in range(1, v + 1):
            bfs(u)

        print("YES" if isBinary() else "NO")