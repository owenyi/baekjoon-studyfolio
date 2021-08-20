# bfs

from collections import deque

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[True] * M for _ in range(N)]
    warms = []
    for _ in range(K):
        x, y = map(int, input().split())
        warms.append((x, y))
        visited[y][x] = False
    cnt = 0
    for x, y in warms:
        if visited[y][x]: continue
        cnt += 1
        queue = deque([(x, y)])
        visited[y][x] = True
        while queue:
            x, y = queue.popleft()
            if x - 1 > -1 and not visited[y][x - 1]:
                queue.append((x - 1, y))
                visited[y][x - 1] = True
            if x + 1 < M and not visited[y][x + 1]:
                queue.append((x + 1, y))
                visited[y][x + 1] = True
            if y - 1 > -1 and not visited[y - 1][x]:
                queue.append((x, y - 1))
                visited[y - 1][x] = True
            if y + 1 < N and not visited[y + 1][x]:
                queue.append((x, y + 1))
                visited[y + 1][x] = True
    print(cnt)