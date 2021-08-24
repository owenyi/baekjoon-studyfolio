from collections import deque

def bfs(r, c):
    board[r][c] = 0
    queue = deque([(r, c)])
    cnt = 1
    while queue:
        r, c = queue.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < N:
                if board[nr][nc] == 1:
                    queue.append((nr, nc))
                    board[nr][nc] = 0
                    cnt += 1
    return cnt

N = int(input())
board = [list(map(int, list(input()))) for _ in range(N)]

d = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

cnt = 0
result = []
for r in range(N):
    for c in range(N):
        if board[r][c] == 1:
            cnt += 1
            result.append(bfs(r, c))
print(cnt)
for x in sorted(result):
    print(x)