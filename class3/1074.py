N, r, c = map(int, input().split())
answer = 0
for i in range(N, 0, -1):
    if r >= 2**(i - 1):
        r -= 2**(i - 1)
        answer += 2**(2 * i - 1)
    if c >= 2**(i - 1):
        c -= 2**(i - 1)
        answer += 2**(2 * i - 2)
print(answer)