string = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

answer = 0
i = 0
while i < len(string):
    flag = False
    for j in range(2, 4):
        if string[i:i+j] in croatia:
            flag = True
            break
    answer += 1
    if flag: i += j
    else: i += 1

print(answer)