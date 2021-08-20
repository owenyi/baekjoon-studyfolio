from collections import deque

def bfs(v, t):
    queue = deque([v])
    cnt = 0
    while True:
        for _ in range(len(queue)):
            now = queue.popleft()
            if now == t: return cnt
            for x in link[now]:
                queue.append(x)
        cnt += 1
    return cnt

def kb():
    answer = []
    for i in range(1, N + 1):
        sum = 0
        for j in range(1, N + 1):
            if i == j: continue
            sum += bfs(i, j)
        answer.append(sum)
    return answer

N, M = map(int, input().split())

link = [[] for _ in range(N + 1)]
for _ in range(M):
    a, b = map(int, input().split())
    link[a].append(b)
    link[b].append(a)
result = kb()
print(result.index(min(result)) + 1)