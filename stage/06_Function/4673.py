def d(n):
    sum = n
    while n > 0:
        sum += n % 10
        n //= 10
    return sum

self_nums = [True] * (10001)

for i in range(1, 9999):
    di = d(i)
    if di <= 10000: self_nums[di] = False

for i in range(1, 10001):
    if self_nums[i]: print(i)