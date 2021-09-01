def solution(rows, columns, queries):
    # nums = [[j for j in range(i, i + columns)] for i in range(1, rows**2, rows)]
    nums = [[j for j in range(i, i + columns)] for i in range(1, rows*columns, columns)]

    answer = []
    d = [(0, +1), (+1, 0), (0, -1), (-1, 0)]
    for y1, x1, y2, x2 in queries:
        x, y = x1 - 1, y1 - 1
        _min = nums[y][x]
        temp = _min
        chk = 0
        while True:
            dx, dy = d[chk]
            nx, ny = x + dx, y + dy
            if x == x1 and y == y1 - 1:
                nums[y][x] = temp
                break
            if x1 - 2 < nx < x2 and y1 - 2 < ny < y2:
                next = nums[ny][nx]
                if _min > next:
                    _min = next
                nums[y][x] = next
                x, y = nx, ny
            else:
                chk += 1
        answer.append(_min)

    return answer

rows = 6
columns = 6
queries = [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(rows, columns, queries))