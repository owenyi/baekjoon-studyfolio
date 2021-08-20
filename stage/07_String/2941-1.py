string = input()

croatia = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]

for x in croatia:
    string = string.replace(x, '_')

print(len(string))