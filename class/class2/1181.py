n = int(input())
str_list = []
for i in range(n):
    str_list.append(input())
str_list = list(set(str_list))
# for i in range(n):
#     str = input()
#     if str_list.count(str) == 0:
#         str_list.append(str)

str_list.sort()

str_list.sort(key=len)
# n = len(str_list)
# for i in range(n):
#     for j in range(0, n - 1 - i):
#         if len(str_list[j]) > len(str_list[j + 1]):
#             str_list[j], str_list[j + 1] = str_list[j + 1], str_list[j]
for x in str_list:
    print(x)