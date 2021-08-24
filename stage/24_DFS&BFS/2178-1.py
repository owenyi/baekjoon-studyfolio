from collections import deque

def bfs():
    queue = deque([(0, 0)])
    while queue:
        r, c = queue.popleft()
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < M:
                if board[nr][nc] == 1:
                    queue.append((nr, nc))
                    board[nr][nc] += board[r][c]

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]
    d = [(+1, 0), (0, +1), (-1, 0), (0, -1)]
    bfs()
    print(board[N - 1][M - 1])