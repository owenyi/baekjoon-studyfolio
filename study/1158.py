from collections import deque

N, K = map(int, input().split())
answer = []
queue = deque([str(i) for i in range(1, N + 1)])
for _ in range(N):
    queue.rotate(-(K - 1))
    answer.append(queue.popleft())
print('<' + ", ".join(answer) + '>')