import heapq
INF = int(1e9)


def dijkstra(start):
    pq = []

    heapq.heappush(pq, (0, start))

    while pq:
        now_d, now_v = heapq.heappop(pq)
        # (*중요) 현재 노드가 이전에 처리되었으면 무시
        if distance[now_v] < now_d: continue
        for next_v, cost in graph[now_v]:
            next_d = now_d + cost
            if next_d < distance[next_v]:
                distance[next_v] = next_d
                heapq.heappush(pq, (next_d, next_v))


n = 0
m = 0
start = 0
graph = [[], []] # graph[a] = b, cost

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n + 1)