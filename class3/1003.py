T = int(input())
answer = [[1, 0]]
for _ in range(T):
    N = int(input())
    one = 0
    zero = 1
    tmp = 0
    for _ in range(N):
        one += zero
        zero = tmp
        tmp = one
    print(zero, one)