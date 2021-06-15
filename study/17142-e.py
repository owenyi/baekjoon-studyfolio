from collections import deque
from itertools import combinations
from copy import deepcopy

N, M = map(int, input().split())
visited_mold = [[False] * N for _ in range(N)]
virus = []
for y in range(N):
    row = list(map(int, input().split()))
    for x in range(N):
        if row[x] == 1: visited_mold[y][x] = True
        elif row[x] == 2:
            virus.append((x, y, 0))
            visited_mold[y][x] = True

d_list = [(-1, 0), (1, 0), (0, -1), (0, 1)]
min_time = int(1e9)
for comb in combinations(virus, M):
    visited = deepcopy(visited_mold)
    queue = deque(comb)
    while queue:
        x, y, cnt = queue.popleft()
        for dx, dy in d_list:
            nx, ny = x + dx, y + dy
            if -1 < nx < N and -1 < ny < N and not visited[ny][nx]:
                queue.append((nx, ny, cnt + 1))
                visited[ny][nx] = True
    if sum([sum(x) for x in visited]) == N**2:
        if min_time > cnt: min_time = cnt
if min_time == int(1e9): print(-1)
else: print(min_time)