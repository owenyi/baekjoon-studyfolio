def is_han_num(n):
    if n < 100: return True
    n = str(n)
    d = int(n[0]) - int(n[1])
    for i in range(1, len(n) - 1):
        if int(n[i]) - int(n[i + 1]) != d:
            return False
    return True

N = int(input())

cnt = 0
for i in range(1, N + 1):
    if is_han_num(i): cnt += 1

print(cnt)