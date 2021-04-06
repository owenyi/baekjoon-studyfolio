K, N = map(int, input().split())
nums = [int(input()) for _ in range(K)]

left, right = 1, max(nums)

while left <= right:
    mid = (left + right) // 2
    sum = 0
    for x in nums:
        sum += x // mid
    if sum < N: # mid too big   left...target...mid
        right = mid - 1
    elif sum >= N: # mid too small
        left = mid + 1

print(right)