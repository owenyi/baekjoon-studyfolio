T = int(input())
answer = [[1, 0]]
for _ in range(T):
    N = int(input())
    zero = 1
    one = 0
    tmp = zero
    for _ in range(N):
        zero = one
        one += tmp
        tmp = zero
    print(zero, one)