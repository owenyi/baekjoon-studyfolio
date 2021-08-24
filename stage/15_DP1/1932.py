n = int(input())
memos = [int(input())]
for i in range(2, n + 1):
    nums = list(map(int, input().split()))
    memos.append(memos[-1] + nums[-1])
    for j in range(i - 2, 0, -1):
        memos[j] = nums[j] + max(memos[j - 1:j + 1])
    memos[0] += nums[0]
print(max(memos))