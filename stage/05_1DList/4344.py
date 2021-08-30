C = int(input())
for _ in range(C):
    nums = list(map(int, input().split()))
    avg = sum(nums[1:]) / nums[0]
    cnt = 0
    for x in nums[1:]:
        if x > avg: cnt += 1
    print(f"{cnt / nums[0] * 100:.3f}%")