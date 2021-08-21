import sys
input = sys.stdin.readline
from collections import deque

N = int(input())
queue = deque()
answer = []
for _ in range(N):
    _input = input().split()
    cmd = _input[0]
    if cmd == "push": queue.append(int(_input[1]))
    elif cmd == "pop": answer.append(queue.popleft() if queue else -1)
    elif cmd == "size": answer.append(len(queue))
    elif cmd == "empty": answer.append(1 * (not queue))
    elif cmd == "front": answer.append(queue[0] if queue else -1)
    elif cmd == "back": answer.append(queue[-1] if queue else -1)

print('\n'.join(answer))