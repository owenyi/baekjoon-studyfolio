N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]

result = 0
for coin in coins[::-1]:
    result += K // coin
    K %= coin

print(result)