N, K = map(int, input().split())
seq = []
nums = [i for i in range(N)]
nums[0] = N
next = 0
for _ in range(N):
    next = (next + K) % len(nums)
    seq.append(nums.pop(next))
    next -= 1
seq = str(seq)
print('<' + seq[1:-1] + '>')