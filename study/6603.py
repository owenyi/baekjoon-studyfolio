from itertools import combinations

while True:
    _input = input()
    if _input == '0': break
    nums = list(map(int, _input[2:].split()))
    comb_list = list(combinations(nums, 6))
    for comb in comb_list:
        for c in comb:
            print(c, end=' ')
        print()
    print()