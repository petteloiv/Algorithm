import sys
sys.stdin=open('input.txt')

T = int(input())

for i in range(T):
    stack = []
    lst = list(input())
    # print(lst)

    for j in range(len(lst)):
        if lst[j] == '(':
            stack.append('(')
        elif lst[j] == ')':
            if len(stack) == 0:
                print('NO')
                break
            else:
                stack.pop()

        if j == len(lst)-1 and len(stack) == 0:
            print('YES')

        elif j == len(lst)-1 and len(stack) > 0:
            print('NO')