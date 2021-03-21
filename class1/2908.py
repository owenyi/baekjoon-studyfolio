A, B = map(int, input().split())
def reverse(x):
    return x // 100 + x % 100 // 10 * 10 + x % 10 * 100
max = max(reverse(A), reverse(B))
print(max)