import heapq

INF = int(1e9) # 10억
d_list = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def dijkstra(start_r, start_c):
    distance[start_r][start_c] = 0
    q = []
    heapq.heappush(q, (0, start_r, start_c))
    while q:
        cost, r, c = heapq.heappop(q)
        if distance[r][c] < cost: continue # 시간을 빠르게 하기 위한 한 줄
        for dr, dc in d_list:
            nr, nc = r + dr, c + dc
            if -1 < nr < n and -1 < nc < n:
                d = board[nr][nc] + cost
                if d < distance[nr][nc]:
                    distance[nr][nc] = d
                    heapq.heappush(q, (d, nr, nc))

n = int(input())
board = []
for _ in range(n):
    board.append(list(map(lambda x: (int(x) + 1) % 2, list(input()))))
distance = [[INF] * n for _ in range(n)]

dijkstra(0, 0)
print(distance[n - 1][n - 1])