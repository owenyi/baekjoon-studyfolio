# combinations 직접 구현

def combinations(nums, n):
    check = [0] * (len(nums) + 1)
    comb_list = []
    comb = []
    def combination(start):
        if len(comb) == n:
            comb_list.append(comb.copy())
            return
        for i in range(start, len(nums)):
            if check[i] == 1: continue
            check[i] = 1
            comb.append(nums[i])
            combination(i)
            check[i] = 0
            del comb[-1]
    combination(0)
    return comb_list

while True:
    _input = input()
    if _input == '0': break
    nums = list(map(int, _input[2:].split()))
    comb_list = combinations(nums, 6)
    for comb in comb_list:
        for c in comb:
            print(c, end=' ')
        print()
    print()