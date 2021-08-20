from collections import deque

K = int(input())
stack = deque()
for _ in range(K):
    n = int(input())
    if n: stack.append(n)
    else: stack.pop()
print(sum(stack))