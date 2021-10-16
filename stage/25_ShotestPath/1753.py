from heapq import heappush, heappop
INF = int(1e9)

v, e = map(int, input().split())

start = int(input())

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

distance = [INF] * (v + 1)

def dijkstra(start):
    pq = [(0, start)]
    distance[start] = 0

    while pq:
        now_d, now_v = heappop(pq)
        if now_d < distance[now_v]: continue
        for next_v, cost in graph[now_v]:
            next_d = now_d + cost
            if next_d < distance[next_v]:
                heappush(pq, (next_d, next_v))
                distance[next_v] = next_d

dijkstra(start)

for d in distance[1:]:
    if d == INF: print("INF")
    else: print(d)