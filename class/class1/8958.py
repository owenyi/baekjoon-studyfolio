N = int(input())
for i in range(N):
    ox = input()
    sum, count = 0, 0
    for x in ox:
        if x == 'O': count += 1
        if x == 'X': count = 0
        sum += count
    print(sum)