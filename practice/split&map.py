# 1. "40 80 60".split() -> str의 list ex) ["40", "80", "60"]
# 2-1. a, b, c = map(int, nums) -> a, b, c가 각각 int로 바뀜 ex) a = 40, b = 80, c = 60
# 2-2. numList = list(map(int, nums)) -> numList가 int의 list ex) [40, 80, 60]

numStr = "10 20 30"
nums = numStr.split()
print(nums) # ["10", "20", "30"]

# numStr2 = input()
# nums2 = numStr2.split()
# print(nums2)

a, b, c = map(int, nums)
print(a, b, c)

print(map(int, nums))
print(list(map(int, nums)))

# input()       split()               map(int, ...)              list(...)
# "40 80 60" -> ["40", "80", "60"] -> 40 80 60...map에 들어있음 -> [40, 80, 60]
list = list(map(int, input().split()))
print(list)