import sys
input = sys.stdin.readline

N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

for x in sorted(nums):
    print(x)