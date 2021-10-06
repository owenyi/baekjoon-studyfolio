from itertools import combinations

N = int(input())

status_matrix = []
for _ in range(N):
    status_array = list(map(int, input().split(' ')))
    status_matrix.append(status_array)

_min = int(1e9)
for start_list in combinations(range(N), N // 2):
    start_set = set(start_list)
    link_set = set(range(N)) - start_set
    start_sum, link_sum = 0, 0
    for i, j in combinations(start_set, 2):
        start_sum += status_matrix[i][j] + status_matrix[j][i]
    for i, j in combinations(link_set, 2):
        link_sum += status_matrix[i][j] + status_matrix[j][i]
    _new = abs(start_sum - link_sum)
    if _min > _new:
        _min = _new
print(_min)