from collections import deque

def bfs():
    queue = deque()
    for r in range(R):
        for c in range(C):
            if board[r][c] == 1:
                queue.append((0, r, c))

    # N = len(queue) # 필요 없음

    d = [(-1, 0), (+1, 0), (0, -1), (0, +1)]

    while queue:
        cnt, r, c = queue.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if -1 < nr < R and -1 < nc < C:
                if board[nr][nc] == 0:
                    queue.append((cnt + 1, nr, nc))
                    board[nr][nc] = 1

    for r in range(R):
        for c in range(C):
            if board[r][c] == 0:
                return -1

    return cnt

C, R = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(R)]

print(bfs())