import sys
sys.setrecursionlimit(11)


def make_star(n):
    if n == 1: return ['*']

    recur = make_star(n//3)
    stars = []

    for x in recur:
        stars.append(x*3)
    for x in recur:
        stars.append(x + ' '*(n//3) + x)
    for x in recur:
        stars.append(x*3)
    return stars


n = int(sys.stdin.readline())
print('\n'.join(make_star(n)))