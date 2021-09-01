import sys

def fib(n):
    if n < len(memo): return memo[n]
    return fib(n - 1) + fib(n - 2)

memo = [0, 1]

n = int(sys.stdin.readline())

print(fib(n))
