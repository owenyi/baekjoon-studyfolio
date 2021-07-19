import heapq
import sys
input = sys.stdin.readline

INF = int(1e9) # 10억

def dijkstra(start):
    distance[start] = 0
    q = []
    heapq.heappush(q, (0, start))
    while q:
        c_now, now = heapq.heappop(q)
        for next, c_next in graph[now]:
            d = c_next + c_now
            if d < distance[next]:
                distance[next] = d
                heapq.heappush(q, (d, next))

v, e = map(int, input().split())
start = int(input())

distance = [INF] * (v + 1)

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

dijkstra(start)
for x in distance[1:]:
    if x == INF: print("INF")
    else: print(x)