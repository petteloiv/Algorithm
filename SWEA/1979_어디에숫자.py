import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행우선순회
    row = 0
    for i in range(N):
        cnt = 0
        for j in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    row += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            row += 1


    # 열 우선순회
    col = 0
    for j in range(N):
        cnt = 0
        for i in range(N):
            if arr[i][j] == 0:
                if cnt == K:
                    col += 1
                cnt = 0
            else:
                cnt += 1
        if cnt == K:
            col += 1

    print(f'#{tc} {row+col}')