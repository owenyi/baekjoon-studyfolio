def solution(enroll, referral, seller, amount):
    N = len(enroll)

    graph = {enroll[i]: i for i in range(N)}

    answer = [0] * N
    for x, y in zip(seller, amount):
        y *= 100
        while True:
            next = referral[graph[x]]
            remain = y // 10
            answer[graph[x]] += y - remain
            # if next == '-': break
            if remain == 0 or next == '-': break
            x = next
            y = remain

    return answer