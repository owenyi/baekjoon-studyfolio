str = input().upper()
alpha = [0] * 26
for x in str:
    alpha[ord(x) - 65] += 1
max = max(alpha)
if alpha.count(max) > 1: print('?')
else: print(chr(alpha.index(max) + 65))