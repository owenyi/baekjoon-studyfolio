def distance(pair):
    (r1, c1), (r2, c2) = pair
    return abs(r1 - r2) + abs(c1 - c2)


def comb(people, r):
    nearby = []
    visited = [False] * len(people)

    def generate(chosen, start, r):
        if r == 0:
            if distance(chosen) <= 2:
                nearby.append(chosen.copy())
            return
        n = len(people)
        for i in range(start, n):
            if not visited[i]:
                visited[i] = True
                chosen.append(people[i])
                generate(chosen, i, r - 1)
                chosen.remove(people[i])
                visited[i] = False

    generate([], 0, r)
    return nearby


def well_distanced(nearby, place):
    for pair in nearby:
        flag = True
        if distance(pair) == 1:
            return 0
        else:
            (r1, c1), (r2, c2) = pair
            if r1 == r2:
                if place[r1][(c1 + c2) // 2] != 'X':
                    flag = False
            elif c1 == c2:
                if place[(r1 + r2) // 2][c1] != 'X':
                    flag = False
            elif place[r1][c2] != 'X' or place[r2][c1] != 'X':
                flag = False
        if not flag:
            return 0
    return 1


def solution(places):
    answer = []
    for place in places:
        people = []
        for i in range(5):
            for j in range(5):
                if place[i][j] == 'P':
                    people.append((i, j))
        nearby = comb(people, 2)
        answer.append(well_distanced(nearby, place))
    return answer


places = [["POOOP",
           "OXXOX",
           "OPXPX",
           "OOXOX",
           "POXXP"],
          # ["POOPX",
          #  "OXPXP",
          #  "PXXXO",
          #  "OXXXO",
          #  "OOOPP"],
          # ["PXOPX",
          #  "OXOXP",
          #  "OXPOX",
          #  "OXXOP",
          #  "PXPOX"],
          # ["OOOXX",
          #  "XOOOX",
          #  "OOOXX",
          #  "OXOOX",
          #  "OOOOO"],
          ["PXPXP",
           "XPXPX",
           "PXPXP",
           "XPXPX",
           "PXPXP"]]
print(solution(places))