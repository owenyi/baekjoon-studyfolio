from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
stack = deque()
for _ in range(N):
    cmds = input().split()
    if cmds[0] == "push":
        stack.append(cmds[1])
    elif cmds[0] == "pop":
        if stack: print(stack.pop())
        else: print(-1)
    elif cmds[0] == "size":
        print(len(stack))
    elif cmds[0] == "empty":
        if stack: print(0)
        else: print(1)
    elif cmds[0] == "top":
        if stack: print(stack[-1])
        else: print(-1)