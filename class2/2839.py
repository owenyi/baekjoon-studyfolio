N = int(input())
cnt = 0
while True:
    if N % 5 == 0:
        print(cnt + (N // 5))
        break
    if N != 3 and N < 5:
        print(-1)
        break
    N -= 3
    cnt += 1