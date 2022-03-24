import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    n = int(input())
    lst = list(int(input()) for _ in range(n))
    # print(lst)

    cnt = 0
    maxheight = 0

    for i in range(n - 1, -1, -1):
        if lst[i] > maxheight:
            cnt += 1
            maxheight = lst[i]

    print(f'#{tc} {cnt}')