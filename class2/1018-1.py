N, M = map(int, input().split())
chess = []
for _ in range(N):
    chess.append(list(input()))

answer = 64
for i in range(N - 7):
    for j in range(M - 7):
        cnt = 0
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if (k + l) % 2 == 0 and chess[k][l] != 'W':
                    cnt += 1
                if (k + l) % 2 == 1 and chess[k][l] != 'B':
                    cnt += 1
        if answer > min(cnt, 64 - cnt): answer = min(cnt, 64 - cnt)
print(answer)