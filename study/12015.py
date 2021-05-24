N = int(input())
A = list(map(int, input().split()))
B = [A[0]]
for x in A[1:]:
    if B[-1] < x:
        B.append(x)
    else:
        l, r = 0, len(B) - 1
        while l <= r:
            m = (l + r) // 2
            if B[m] >= x: r = m - 1
            else: l = m + 1
        B[l] = x
print(len(B))