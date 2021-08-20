N, M, B = map(int, input().split())
hList = []
for _ in range(N):
    hList += list(map(int, input().split()))
hList.sort()
minTime = (sum(hList) - (hList[0] * M * N)) * 2
height = hList[0]
for i in range(hList[0] + 1, hList[-1] + 1):
    under, high = 0, 0
    for j in range(0, len(hList)):
        if hList[j] - i < 0: under += i - hList[j]
        elif hList[j] - i > 0: high += hList[j] - i
    if high + B >= under:
        if high * 2 + under <= minTime:
            minTime = high * 2 + under
            height = i
    else: break
print(minTime, height)
