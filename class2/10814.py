N = int(input())
infos = [input().split() for _ in range(N)]
infos.sort(key=lambda x: int(x[0]))
for age, name in infos:
    print(age, name)