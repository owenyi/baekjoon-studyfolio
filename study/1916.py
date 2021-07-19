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
        if distance[now] < c_now: continue # 시간을 빠르게 하기 위한 한 줄
        for next, c_next in graph[now]:
            d = c_next + c_now
            if d < distance[next]:
                distance[next] = d
                heapq.heappush(q, (d, next))

v = int(input())
e = int(input())

distance = [INF] * (v + 1)

graph = [[] for _ in range(v + 1)]
for _ in range(e):
    a, b, cost = map(int, input().split())
    graph[a].append((b, cost))

start, end = map(int, input().split())

dijkstra(start)
print(distance[end])