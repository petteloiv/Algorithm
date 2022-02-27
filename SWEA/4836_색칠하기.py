import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    red = []
    blue = []
    arr = [[0]*10 for _ in range(10)]

    for n in range(N):
        x1, y1, x2, y2, colour = map(int, input().split())
        if colour == 1:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if [i,j] not in red:
                        arr[i][j] += 1
                        red.append([i,j])
        else:
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if [i, j] not in blue:
                        arr[i][j] += 2
                        blue.append([i, j])

    cnt = 0
    for ii in range(10):
        for jj in range(10):
            if arr[ii][jj] == 3:
                cnt += 1


    print(f'#{tc} {cnt}')
