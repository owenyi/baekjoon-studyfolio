from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deque = deque()
for _ in range(N):
    cmds = input().split()
    if cmds[0] == "push_front":
        deque.appendleft(cmds[1])
    elif cmds[0] == "push_back":
        deque.append(cmds[1])
    elif cmds[0] == "pop_front":
        if deque: print(deque.popleft())
        else: print(-1)
    elif cmds[0] == "pop_back":
        if deque: print(deque.pop())
        else: print(-1)
    elif cmds[0] == "size":
        print(len(deque))
    elif cmds[0] == "empty":
        if deque: print(0)
        else: print(1)
    elif cmds[0] == "front":
        if deque: print(deque[0])
        else: print(-1)
    elif cmds[0] == "back":
        if deque: print(deque[-1])
        else: print(-1)