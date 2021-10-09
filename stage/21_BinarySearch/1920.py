def binary_search(key):
    l, r = 0, N - 1
    while l <= r:
        m = (l + r) // 2
        if targets[m] == key: return 1
        elif targets[m] > key: r = m - 1
        elif targets[m] < key: l = m + 1
    return 0

N = int(input())
targets = list(map(int, input().split()))
targets.sort()

M = int(input())
keys = map(int, input().split())
for key in keys:
    print(binary_search(key))