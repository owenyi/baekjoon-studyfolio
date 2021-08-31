import sys

T = int(sys.stdin.readline())
for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, sys.stdin.readline().split())
    dc = ((x2 - x1)**2 + (y2 - y1)**2)**.5
    if dc == 0 and r1 == r2: print(-1)
    elif dc == r1 + r2 or dc == abs(r2 - r1): print(1)
    elif max(dc, r1, r2) > sum([dc, r1, r2]) - max(dc, r1, r2): print(0)
    else: print(2)