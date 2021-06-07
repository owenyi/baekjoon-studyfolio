import sys
sys.setrecursionlimit(10**5)

def dfs(x, y):
    if visited[y][x]: return 0
    visited[y][x] = True
    if x - 1 > -1 and not visited[y][x - 1]: dfs(x - 1, y)
    if x + 1 < M and not visited[y][x + 1]: dfs(x + 1, y)
    if y - 1 > -1 and not visited[y - 1][x]: dfs(x, y - 1)
    if y + 1 < N and not visited[y + 1][x]: dfs(x, y + 1)
    return 1

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
    for x, y in warms: cnt += dfs(x, y)
    print(cnt)