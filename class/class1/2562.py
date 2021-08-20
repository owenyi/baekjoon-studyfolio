max, maxIdx = 0, 0
for i in range(9):
    num = int(input())
    if num > max: max, maxIdx = num, i + 1

print(max)
print(maxIdx)