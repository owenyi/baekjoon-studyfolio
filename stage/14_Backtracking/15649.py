def permutations(seq, n):
    seq.sort()

    length = len(seq)
    visited = [False] * length
    generator = []
    def generate(depth):
        if depth == n:
            print(' '.join(map(str, generator)))
            return
        for i in range(length):
            if not visited[i]:
                visited[i] = True
                generator.append(seq[i])
                generate(depth + 1)
                del generator[-1]
                visited[i] = False

    generate(0)

if __name__ == "__main__":
    N, M = map(int, input().split())
    permutations(list(range(1, N + 1)), M)