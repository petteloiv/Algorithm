import sys; sys.stdin = open('input.txt',encoding='utf-8')

T = int(input())

for tc in range(1,T+1):
    stack = []
    lst = []

    while True:
        a = input()
        if a == '문제':
            stack.append(a)
        elif a == '고무오리':
            if len(stack) == 0:
                stack.append('문제')
                stack.append('문제')
            else:
                stack.pop()
        elif a == '고무오리 디버깅 끝':
            break

    if len(stack) == 0:
        print('고무오리야 사랑해')
    else:
        print('힝구')

