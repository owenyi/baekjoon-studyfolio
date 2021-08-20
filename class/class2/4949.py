from collections import deque

def isBalanced(s):
    stack = deque()
    for x in s:
        if x == "(": stack.append(1)
        elif x == "[": stack.append(2)
        elif x == ")":
            if not stack or stack.pop() != 1: return False
        elif x == "]":
            if not stack or stack.pop() != 2: return False
    if stack: return False
    return True

while True:
    s = input()
    if s == '.': break
    if isBalanced(s): print("yes")
    else: print("no")