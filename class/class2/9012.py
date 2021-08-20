def VPS(line):
    cnt = 0
    for x in line:
        if x == '(': cnt += 1
        else:
            if cnt: cnt -= 1
            else: return 'NO'
    if cnt: return 'NO'
    else: return 'YES'

T = int(input())
for _ in range(T):
    line = input()
    print(VPS(line))