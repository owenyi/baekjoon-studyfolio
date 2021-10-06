def solution():
    n = N // 2
    starts = []

    def generate(start, depth):
        if depth == n:
            links = list(candidates - set(starts))
            _new = 0
            def comb_two_sum(seq):
                _sum = 0
                for i in range(n):
                    for j in range(i + 1, n):
                        _sum += S[seq[i]][seq[j]] + S[seq[j]][seq[i]]
                return _sum
            _new = abs(comb_two_sum(starts) - comb_two_sum(links))
            global _min
            if _min > _new:
                _min = _new

        for next in range(start, N):
            starts.append(next)
            generate(next + 1, depth + 1)
            del starts[-1]

    generate(0, 0)

if __name__ == "__main__":
    N = int(input())

    S = []
    for _ in range(N):
        s = list(map(int, input().split(' ')))
        S.append(s)

    candidates = set(range(N))

    _min = int(1e9)

    solution()
    print(_min)