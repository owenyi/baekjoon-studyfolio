remainders = [0] * 42
for _ in range(10):
    n = int(input())
    remainders[n % 42] = 1
print(remainders.count(1))