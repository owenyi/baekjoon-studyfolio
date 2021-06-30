import heapq
import sys
input = sys.stdin.readline

N = int(input())
infos = [tuple(map(int, input().split())) for _ in range(N)]
infos.sort()
# print(infos)
target, able = map(int, input().split())
current = 0

q = []

cnt = 0
flag = True
i = 0
while able < target:
    while i < N and infos[i][0] <= able:
        heapq.heappush(q, (-infos[i][1], infos[i][0]))
        i += 1
    if q:
        able_plus, current = heapq.heappop(q)
        able += -able_plus # gas값이 최대힙으로 쓰이기 위해 음수로 들어갔음
        cnt += 1
    else:
        flag = False
        break
    # print(current, able)
if flag: print(cnt)
else: print(-1)