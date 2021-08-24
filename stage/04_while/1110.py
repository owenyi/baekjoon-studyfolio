N = int(input())
temp = N
cnt = 0
while True:
    temp = temp % 10 * 10 + (temp % 10 + temp // 10) % 10
    cnt += 1
    if temp == N: break
print(cnt)