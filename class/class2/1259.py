def isPal(x):
    n = len(x)
    for i in range(n):
        if x[i] != x[n - 1 - i]:
            return False
    return True

while True:
    num = input()
    if num == '0': break
    if isPal(num): print("yes")
    else: print("no")