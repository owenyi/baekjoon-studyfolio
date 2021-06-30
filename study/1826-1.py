import heapq
import sys
input = sys.stdin.readline

N = int(input())
infos = [tuple(map(int, input().split())) for _ in range(N)]
infos.sort()
# print(infos)
target, remain = map(int, input().split())
infos.append((target, -1))
current = 0

q = []

cnt = 0
location = 0
flag = True
for i in range(N + 1):
    remain -= infos[i][0] - location
    while q and remain < 0:
        remain += -heapq.heappop(q)
        cnt += 1
    if remain < 0:
        flag = False
        break
    if remain == -1: break
    location = infos[i][0]
    heapq.heappush(q, -infos[i][1])
if flag: print(cnt)
else: print(-1)