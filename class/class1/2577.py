A = int(input())
B = int(input())
C = int(input())
result = str(A * B * C)
counts = [0] * 10
for x in result:
    counts[int(x)] += 1
for x in counts:
    print(x)
