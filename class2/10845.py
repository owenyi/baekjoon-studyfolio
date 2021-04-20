from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
queue = deque()
for _ in range(N):
    cmds = input().split()
    if cmds[0] == "push":
        queue.append(cmds[1])
    elif cmds[0] == "pop":
        if queue: print(queue.popleft())
        else: print(-1)
    elif cmds[0] == "size":
        print(len(queue))
    elif cmds[0] == "empty":
        if queue: print(0)
        else: print(1)
    elif cmds[0] == "front":
        if queue: print(queue[0])
        else: print(-1)
    elif cmds[0] == "back":
        if queue: print(queue[-1])
        else: print(-1)