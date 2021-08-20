def permutation(depth):
    global s
    if depth == M:
        perm.append(s)
        return
    for i in range(1, N + 1):
        s += f"{i} "
        permutation(depth + 1)
        s = s[:-2]

if __name__ == "__main__":
    N, M = map(int, input().split())
    perm = []
    s = ""

    permutation(0)
    for x in perm:
        print(x)