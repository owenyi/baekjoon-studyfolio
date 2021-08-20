from collections import deque

def worm(y, x):
    if visited[y][x]: return 0
    else: visited[y][x] = True
    if y - 1 > -1: worm(y - 1, x)
    if y + 1 < N: worm(y + 1, x)
    if x - 1 > -1: worm(y, x - 1)
    if x + 1 < M: worm(y, x + 1)
    return 1

T = int(input())
for _ in range(T):
    M, N, K = map(int, input().split())
    visited = [[True] * M for _ in range(N)]
    stack = deque()
    for _ in range(K):
        x, y = map(int, input().split())
        stack.append([y, x])
        visited[y][x] = False
    cnt = 0
    while stack:
        y, x = stack.pop()
        cnt += worm(y, x)
    print(cnt)