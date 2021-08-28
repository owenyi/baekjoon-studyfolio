def group_check(string):
    chks = [False] * 26
    now = ord(string[0]) - 97
    chks[now] = True
    for next in string[1:]:
        next = ord(next) - 97
        if now != next:
            if chks[next] == False:
                chks[next] = True
                now = next
            else: return False
    return True

N = int(input())

result = 0
for _ in range(N):
    string = input()
    result += group_check(string)
print(result)