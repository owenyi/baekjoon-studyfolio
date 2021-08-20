from collections import deque

n = int(input())
queue = deque()
for _ in range(n):
    queue.append(int(input()))

stack = deque()
result = deque()
for i in range(1, n + 1):
    stack.append(i)
    result.append('+')
    while stack:
        if queue[0] == stack[-1]:
            queue.popleft()
            stack.pop()
            result.append('-')
        else: break

if queue:
    print("NO")
else:
    while result:
        print(result.popleft())