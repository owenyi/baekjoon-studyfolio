import heapq
import sys
input = sys.stdin.readline

N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort()

heap = [times[0][1]]

cnt = 1
for start, end in times[1:]:
    if start < heap[0]: cnt += 1
    else: heapq.heappop(heap)
    heapq.heappush(heap, end)
print(cnt)