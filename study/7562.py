from collections import deque

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
        if x-1 > -1 and y-2 > -1 and not visited[y-2][x-1]:
            queue.append((x-1, y-2, cnt + 1))
            visited[y-2][x-1] = True
        if x-2 > -1 and y-1 > -1 and not visited[y-1][x-2]:
            queue.append((x-2, y-1, cnt + 1))
            visited[y-1][x-2] = True
        if x-1 > -1 and y+2 < L and not visited[y+2][x-1]:
            queue.append((x-1, y+2, cnt + 1))
            visited[y+2][x-1] = True
        if x-2 > -1 and y+1 < L and not visited[y+1][x-2]:
            queue.append((x-2, y+1, cnt + 1))
            visited[y+1][x-2] = True
        if x+1 < L and y-2 > -1 and not visited[y-2][x+1]:
            queue.append((x+1, y-2, cnt + 1))
            visited[y-2][x+1] = True
        if x+2 < L and y-1 > -1 and not visited[y-1][x+2]:
            queue.append((x+2, y-1, cnt + 1))
            visited[y-1][x+2] = True
        if x+1 < L and y+2 < L and not visited[y+2][x+1]:
            queue.append((x+1, y+2, cnt + 1))
            visited[y+2][x+1] = True
        if x+2 < L and y+1 < L and not visited[y+1][x+2]:
            queue.append((x+2, y+1, cnt + 1))
            visited[y+1][x+2] = True
    print(cnt)