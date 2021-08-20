N = int(input())
locations = sorted([list(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))
for x, y in locations:
    print(x, y)