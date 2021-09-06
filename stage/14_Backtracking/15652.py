import sys

def comb_with_repet(n, m):
    results = []
    result = []

    def generator(start, depth):
        if depth == m:
            results.append(result.copy())
            return
        for i in range(start, n + 1):
            result.append(i)
            generator(i, depth + 1)
            del result[-1]
    generator(1, 0)

    return results

N, M = map(int, sys.stdin.readline().split())

results = comb_with_repet(N, M)

answer = ""
for x in results:
    answer += f"{' '.join(map(str, x))}\n"
print(answer)