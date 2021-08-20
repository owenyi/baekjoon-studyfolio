from collections import Counter

N = int(input())
cards = Counter(input().split())
M = int(input())
nums = input().split()
for x in nums:
    print(cards[x], end=' ')