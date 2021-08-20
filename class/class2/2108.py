from collections import Counter
import sys

input = sys.stdin.readline

N = int(input())
# nums = []
# for _ in range(N):
#     nums.append(int(input()))
nums = sorted([int(input()) for _ in range(N)])
print(round(sum(nums) / N))
print(nums[N // 2])
counter = Counter(nums).most_common(2)
if N == 1: print(counter[0][0])
elif counter[0][1] == counter[1][1]:
    print(counter[1][0])
else:
    print(counter[0][0])
print(nums[N - 1] - nums[0])