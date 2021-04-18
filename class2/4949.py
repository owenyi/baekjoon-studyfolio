from collections import deque

def isBalanced(line):
    stack = deque()
    for x in line:
        if x == '(' or x == '[': stack.append(x)
        elif x == ')':
            if not(stack) or '(' != stack.pop(): return 'no'
        elif x == ']':
            if not(stack) or '[' != stack.pop(): return 'no'
    if stack: return 'no'
    else: return 'yes'

while True:
    line = input()
    if line == '.': break
    print(isBalanced(line))