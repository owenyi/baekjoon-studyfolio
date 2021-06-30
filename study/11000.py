import heapq
import sys
input = sys.stdin.readline

N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
times.sort() # x[1]에 대해는 할 필요가 없음
# print(times)

heap = [times[0][1]]

cnt = 1
for start, end in times[1:]:
    if start < heap[0]: # 시작시간이 힙(end의 힙)의 첫번째 보다 빠르면
        heapq.heappush(heap, end)
        cnt += 1
    else:
        heapq.heappop(heap)
        heapq.heappush(heap, end)
print(cnt)