from collections import deque

n = int(input())
for _ in range(n):
    N, M = map(int, input().split())
    nums = deque(list(map(int, input().split())))
    keys = deque([i for i in range(N)])
    cnt = 0
    now = -1
    while now != M:
        if max(nums) > nums[0]:
            nums.rotate(-1)
            keys.rotate(-1)
        else:
            cnt += 1
            nums.popleft()
            now = keys.popleft()
    print(cnt)