# combinations 직접 구현 - simplified

def combinations(nums, n):
    check = [0] * (len(nums) + 1)
    comb = []
    def combination(start):
        if len(comb) == n:
            for c in comb:
                print(c, end=' ')
            print()
            return
        for i in range(start, len(nums)):
            if check[i] == 1: continue
            check[i] = 1
            comb.append(nums[i])
            combination(i)
            check[i] = 0
            del comb[-1]
    combination(0)
    print()

while True:
    _input = input()
    if _input == '0': break
    nums = list(map(int, _input[2:].split()))
    combinations(nums, 6)