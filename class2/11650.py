N = int(input())
locations = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[0], x[1]))
for x, y in locations:
    print(x, y)