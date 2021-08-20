def permutation():
    global s
    if len(s) == M * 2:
        perm.append(s)
        return
    for i in range(1, N + 1):
        s += f"{i} "
        permutation()
        s = s[:-2]

if __name__ == "__main__":
    N, M = map(int, input().split())
    perm = []
    s = ""

    permutation()
    for x in perm:
        print(x)