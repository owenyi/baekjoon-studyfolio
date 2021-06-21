N = int(input())
distances = list(map(int, input().split()))
costs = list(map(int, input().split()))

min_cost = 1000000000
result = 0
for i in range(N - 1):
    if min_cost > costs[i]: min_cost = costs[i]
    result += distances[i] * min_cost
print(result)