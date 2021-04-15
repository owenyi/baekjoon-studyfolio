def san(sand, y, x):
    global ans
    if 0 <= y < N and 0 <= x < N: mat[y][x] += sand
    else: ans += sand

def tor(sand, dir, y, x):
    mat[y][x] = 0
    sand1 = sand // 100
    sand2 = sand // 50
    sand5 = sand // 20
    sand7 = sand * 7 // 100
    sand10 = sand // 10
    sanda = sand - sand5 - 2 * (sand1 + sand2 + sand7 + sand10)
    if dir == 1:
        san(sand1, y - 1, x + 1); san(sand1, y + 1, x + 1);
        san(sand2, y - 2, x); san(sand2, y + 2, x);
        san(sand7, y - 1, x); san(sand7, y + 1, x);
        san(sand10, y - 1, x - 1); san(sand10, y + 1, x - 1);
        san(sanda, y, x - 1); san(sand5, y, x - 2);
    elif dir == 2:
        san(sand1, y - 1, x - 1); san(sand1, y - 1, x + 1);
        san(sand2, y, x - 2); san(sand2, y, x + 2);
        san(sand7, y, x - 1); san(sand7, y, x + 1);
        san(sand10, y + 1, x - 1); san(sand10, y + 1, x + 1);
        san(sanda, y + 1, x); san(sand5, y + 2, x);
    elif dir == 3:
        san(sand1, y + 1, x - 1); san(sand1, y - 1, x - 1);
        san(sand2, y + 2, x); san(sand2, y - 2, x);
        san(sand7, y + 1, x); san(sand7, y - 1, x);
        san(sand10, y + 1, x + 1); san(sand10, y - 1, x + 1);
        san(sanda, y, x + 1); san(sand5, y, x + 2);
    elif dir == 4:
        san(sand1, y + 1, x - 1); san(sand1, y + 1, x + 1);
        san(sand2, y, x - 2); san(sand2, y, x + 2);
        san(sand7, y, x - 1); san(sand7, y, x + 1);
        san(sand10, y - 1, x - 1); san(sand10, y - 1, x + 1);
        san(sanda, y - 1, x); san(sand5, y - 2, x);

def circuit():
    y, x = N // 2, N // 2
    cnt = 1
    while True:
        for _ in range(cnt):
            if (y, x) == (0, 0): return
            x -= 1
            tor(mat[y][x], 1, y, x)
        for _ in range(cnt):
            y += 1
            tor(mat[y][x], 2, y, x)
        cnt += 1
        for _ in range(cnt):
            x += 1
            tor(mat[y][x], 3, y, x)
        for _ in range(cnt):
            y -= 1
            tor(mat[y][x], 4, y, x)
        cnt += 1

N = int(input())
mat = [list(map(int, input().split())) for _ in range(N)]\

ans = 0
circuit()
print(ans)
