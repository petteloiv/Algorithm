import sys
sys.stdin=open("input.txt")

T = 10

for tc in range(1,11):
    N = int(input())
    lst = list(map(int, input().split()))

    building = 0

    for i in range(2, N-2):
        if lst[i] > max(lst[i-2], lst[i-1], lst[i+1], lst[i+2]):
            m = max(lst[i-2], lst[i-1], lst[i+1], lst[i+2])
            building += lst[i] - m
        else:
            continue


    print(f'#{tc} {building}')