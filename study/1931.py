N = int(input())
times = [tuple(map(int, input().split())) for _ in range(N)]
# print(times)
# times.sort(key=lambda x: (x[0], x[1]))
times.sort(key=lambda x: (x[1], x[0]))
# print(times)

cnt = 1
x, y = times[0]
for nx, ny in times[1:]:
    if nx >= y:
        x, y = nx, ny
        # print(x, y)
        cnt += 1
print(cnt)