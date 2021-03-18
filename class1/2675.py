T = int(input())
for i in range(T):
    num, str = input().split()
    for x in str:
        print(x * int(num), end="")
    print()
