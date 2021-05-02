from collections import Counter

def check1(n, broken): # 0이 들어가면 안 된다.
    while n > 0:
        print(n % 10, n // 10)
        print(broken[n % 10] == 1)
        n //= 10

def check2(n, broken):
    for x in str(n):
        print(x)
        print(broken[x] == 1)

n = 10
broken = Counter([0, 1, 2, 3, 4])
check1(n, broken)
check2(n, broken)
