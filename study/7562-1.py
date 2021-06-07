# dx, dy

from collections import deque

d_list = [(-2, -1), (-1, -2), (-2, 1), (-1, 2), (1, -2), (2, -1), (1, 2), (2, 1)]

for _ in range(int(input())):
    L = int(input())
    visited = [[False] * L for _ in range(L)]
    sx, sy = map(int, input().split()) # start
    tx, ty = map(int, input().split()) # target
    queue = deque([(sx, sy, 0)])
    visited[sy][sx] = True
    while queue:
        x, y, cnt = queue.popleft()
        if x == tx and y == ty: break
        for dx, dy in d_list:
            nx, ny = x + dx, y + dy # next
            if -1 < nx < L and -1 < ny < L and not visited[ny][nx]:
                queue.append((nx, ny, cnt + 1))
                visited[ny][nx] = True
    print(cnt)