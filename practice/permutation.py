def permutations(seq, n):
    seq.sort()
    result = []

    length = len(seq)
    visited = [False] * length
    generator = []
    def generate(depth):
        if depth == n:
            result.append(generator.copy())
            return
        for i in range(length):
            if not visited[i]:
                visited[i] = True
                generator.append(seq[i])
                generate(depth + 1)
                del generator[-1]
                visited[i] = False

    generate(0)

    return result

print(permutations([1, 2, 3, 4], 2))