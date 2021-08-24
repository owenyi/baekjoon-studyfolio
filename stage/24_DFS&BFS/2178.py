from collections import deque

def bfs():
    queue = deque([(1, 0, 0)])
    while queue:
        depth, r, c = queue.popleft()
        if r == N - 1 and c == M - 1: return depth
        for dr, dc in d:
            nr, nc = r + dr, c + dc
            if -1 < nr < N and -1 < nc < M:
                if board[nr][nc] == 1:
                    queue.append((depth + 1, nr, nc))
                    board[nr][nc] = 0

if __name__ == "__main__":
    N, M = map(int, input().split())
    board = [list(map(int, list(input()))) for _ in range(N)]
    d = [(+1, 0), (0, +1), (-1, 0), (0, -1)]
    print(bfs())