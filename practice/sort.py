aList = ["banana", "apple", "kiwi"]

aList.sort()  # 사전 순서
print(aList)

aList.sort(key=len)  # 길이가 작은 것부터
print(aList)

a = [[4, 4], [3, 1], [3, 2], [2, 3], [1, 1]]
print(a)

# a.sort(key=lambda x: x[0]) # index 0 오름차순
# a.sort(key=lambda x: -x[0]) # index 0 내림차순
a.sort(key=lambda x: x[1]) # index 1 오름차순
print(a)
# a.sort(key=lambda x: (x[0], x[1])) # index 1 오름차순 한다음 index 0 오름차순
a.sort(key=lambda x: (x[1], x[0])) # index 0 오름차순 한다음 index 1 오름차순
print(a)