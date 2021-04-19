N = int(input())
sizes = []
for _ in range(N):
    sizes.append(list(map(int, input().split())))
ranks = [1] * N
for i in range(N):
    cnt = 0
    for j in range(N):
        if sizes[i][0] < sizes[j][0] and sizes[i][1] < sizes[j][1]: # index i보다 x, y가 둘 다 큰 j의 개수
            cnt += 1
    ranks[i] += cnt
for rank in ranks:
    print(rank, end=' ')