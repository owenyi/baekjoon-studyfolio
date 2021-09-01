def solution(lottos, win_nums):
    ranks = {2: 5, 3: 4, 4: 3, 5: 2, 6: 1}

    match = 0
    zero = lottos.count(0)
    for x in lottos:
        if x in win_nums:
            match += 1

    rank1 = ranks.get(match + zero)
    rank2 = ranks.get(match)
    return [rank1 if rank1 else 6, rank2 if rank2 else 6]

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]
print(solution(lottos, win_nums))