# input
N = int(input())
schedules = [list(map(int, input().split())) for _ in range(N)]

# sort
schedules.sort(key=lambda x: (x[0], -x[1]))

# make board
coated_papers = [[0] * 366 for _ in range(1001)]
for start, end in schedules:
    for height in range(1, 1001):
        if not coated_papers[height][start]:
            coated_papers[height][start:end+1] = [1] * (end - start + 1)
            for index in range(start, end + 1):
                coated_papers[0][index] = max(coated_papers[0][index], height)
            break

# result
result = 0
max_height = 0
start_index = 0
for index, now_height in enumerate(coated_papers[0] + [0]):
    if now_height == 0:
        if max_height > 0:
            result += (index - start_index) * max_height
            max_height = 0
    elif now_height > max_height:
        if max_height == 0:
            start_index = index
        max_height = now_height
print(result)