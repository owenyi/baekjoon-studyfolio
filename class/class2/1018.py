n, m = map(int, input().split())
wbs = []
for i in range(n):
    row = [x for x in input()]
    wbs.append(row)
min = 64
for i in range(n - 7):
    for j in range(m - 7):
        cnt1 = 0
        cnt2 = 0
        color = wbs[i][j]
        for k in range(i, i + 8):
            for l in range(j, j + 8):
                if ((k - i) + (l - j)) % 2 == 0 and wbs[k][l] != color:
                    cnt1 += 1
                if ((k - i) + (l - j)) % 2 == 1 and wbs[k][l] == color:
                    cnt1 += 1
                if ((k - i) + (l - j)) % 2 == 0 and wbs[k][l] == color:
                    cnt2 += 1
                if ((k - i) + (l - j)) % 2 == 1 and wbs[k][l] != color:
                    cnt2 += 1
        if cnt1 > cnt2: cnt1 = cnt2
        if min > cnt1: min = cnt1
print(min)