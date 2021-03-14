str = input()
alpha = [0] * 26
for x in str:
    if x.isupper(): alpha[ord(x) - 65] += 1
    elif x.islower(): alpha[ord(x) - 97] += 1
max = max(alpha)
if alpha.count(max) > 1: print('?')
else: print(chr(alpha.index(max) + 65))