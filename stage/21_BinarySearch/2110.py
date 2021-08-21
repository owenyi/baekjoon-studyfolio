import sys
input = sys.stdin.readline

N, C = map(int, input().split())
arr = [int(input()) for _ in range(N)]
arr.sort()

l, r = 0, arr[-1] - arr[0]
while l <= r:
    m = (l + r) // 2
    cnt, chk = 1, arr[0]
    for x in arr[1:]:
        if x - chk >= m:
            cnt += 1
            chk = x
    if cnt >= C: l = m + 1
    else: r = m - 1
print(r)