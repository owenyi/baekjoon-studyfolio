alp = [-1] * 26
S = input()
for i in range(len(S)):
    idx = ord(S[i]) - 97
    if alp[idx] == -1: alp[idx] = i
for x in alp:
    print(x, end=' ')
# for x in alp[:-1:]:
#     print(x, end=' ')
# print(alp[-1], end='')