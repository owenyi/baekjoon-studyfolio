n = int(input())
stack = []
i = 1
answer = []
for _ in range(n):
    num = int(input())
    while i <= num:
        answer += '+'
        stack.append(i)
        i += 1
    while stack and stack[-1] == num:
        answer.append('-')
        del stack[-1]
if stack: print("NO")
else:
    for x in answer:
        print(x)


