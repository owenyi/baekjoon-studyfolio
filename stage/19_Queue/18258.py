import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()
for _ in range(N):
    _input = input().split()
    cmd = _input[0]
    if cmd == "push": queue.append(_input[1])
    elif cmd == "pop":
        if queue: print(queue.popleft())
        else: print(-1)
    elif cmd == "size": print(len(queue))
    elif cmd == "empty": print(1* (not queue))
    elif cmd == "front":
        if queue: print(queue[0])
        else: print(-1)
    elif cmd == "back":
        if queue: print(queue[-1])
        else: print(-1)