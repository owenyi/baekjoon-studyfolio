N = int(input())

min = 0
max = 1
sixMul = 6
cnt = 1
while not (min < N <= max):
    min = max
    max += sixMul
    sixMul += 6
    cnt += 1

print(cnt)