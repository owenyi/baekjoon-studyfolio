list = []
for i in range(10):
    num = (int(input())) % 42
    if list.count(num) == 0: list.append(num)
print(len(list))
