r, M = 31, 1234567891
L = int(input())
s = input()
hashes = [1]
for i in range(1, L):
    hashes.append(hashes[-1] * r % M)
sum = 0
for i in range(L):
    sum = (sum + (ord(s[i]) - 96) * hashes[i]) % M
print(sum)