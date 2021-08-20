def find(x):
    l_idx, r_idx = 0, len(A) - 1
    while l_idx <= r_idx:
        m_idx = (l_idx + r_idx) // 2
        if A[m_idx] == x: return 1
        elif A[m_idx] < x: l_idx = m_idx + 1
        elif A[m_idx] > x: r_idx = m_idx - 1
    else: return 0

N = int(input())
A = list(map(int, input().split()))
A.sort()

M = int(input())
B = list(map(int, input().split()))
for x in B: print(find(x))