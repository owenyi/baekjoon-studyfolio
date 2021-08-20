N = int(input())
A = list(map(int, input().split()))
A.sort()

def find(x):
    x = int(x)
    left = 0;
    right = N - 1;
    mid = (left + right) // 2
    while left <= right:
        if A[mid] == x:
            print(1)
            return
        elif A[mid] < x:
            left = mid + 1
        elif A[mid] > x:
            right = mid - 1
        mid = (left + right) // 2
    print(0)

M = int(input())
B = map(find, input().split())
for x in B:
    x