def combinations(seq, n):
    seq.sort()
    result = []
    length = len(seq)

    generator = []
    def generate(start, depth):
        if depth == n:
            result.append(generator.copy())
            return
        for next in range(start, length):
            generator.append(seq[next])
            generate(next + 1, depth + 1)
            del generator[-1]

    generate(0, 0)

    return result

print(combinations([1, 2, 3, 4], 3)) # [[1, 2], [1, 3], [2, 3]]