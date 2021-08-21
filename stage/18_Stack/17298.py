import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))

stack = []
result = []
for x in arr[::-1]:
    while stack and stack[-1] <= x:
        del stack[-1]
    result.append(stack[-1] if stack else -1)
    stack.append(x)

for x in result[::-1]:
    print(x, end=' ')