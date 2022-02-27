import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    num = list(map(int, input().split()))

    minn = 1000000000000000000000000000000000
    maxx = 0
    for i in range(N-M+1):
        add = 0
        for j in range(M):
            add += num[i+j]
        if add > maxx:
            maxx = add
        if add < minn:
            minn = add

    print(f'#{tc} {maxx - minn}')