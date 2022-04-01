# 오타내서 문제 틀림 .. 다섯번이나 ..

import sys
sys.stdin=open('input.txt')


lst = list(map(int, input().split()))
# print(lst)


if lst[0] == 1:
    for i in range(1,len(lst)):
        if lst[i] == lst[i-1] + 1:
            continue
        else:
            print('mixed')
            break
    if i == len(lst)-1:
        print('ascending')


elif lst[0] == 8:
    for i in range(1, len(lst)):
        if lst[i] == lst[i - 1] - 1:
            continue
        else:
            print('mixed')
            break
    if i == len(lst) - 1:
        print('descending')

elif lst[0] != 1 or lst[0] != 8:
    print('mixed')
