import sys

n = int(sys.stdin.readline())

result = []
i = 2
while i <= n:
    if n == 1: break
    if n % i == 0:
        n //= i
        result.append(i)
    else:
        i += 1
for x in result:
    print(x)