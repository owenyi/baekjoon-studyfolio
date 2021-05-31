T = int(input())
for _ in range(T):
    cmd = input()
    n = int(input())
    nums_str = input()
    if n == 0: nums = []
    else: nums = nums_str[1:-1].split(',')
    isReversed = False
    flag = True
    for x in cmd:
        if x == 'R': isReversed = not isReversed
        elif x == 'D':
            if not nums:
                print("error")
                flag = False
                break
            else:
                if isReversed: del nums[-1]
                else: del nums[0]
    if flag:
        if isReversed: print('[' + ','.join(reversed(nums)) + ']')
        else: print('[' + ','.join(nums) + ']')