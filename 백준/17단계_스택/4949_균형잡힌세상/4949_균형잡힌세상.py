import sys
sys.stdin=open('input.txt')

while True:
    lst = input()

    if lst == '.':
        break
    stack = []
    now = True
    for i in lst:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if not stack or stack[-1] == '[':
                now = False
                break
            elif stack[-1] == '(':
                stack.pop()
        elif i == ']':
            if not stack or stack[-1] == '(':
                now = False
                break
            elif stack[-1] == '[':
                stack.pop()
    if now == True and not stack:
        print('yes')
    else:
        print('no')
