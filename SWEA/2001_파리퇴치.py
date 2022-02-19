import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 행 우선 순회
    #
    max_kill = 0
    for x in range(N-M+1):
        for y in range(N-M+1):
            kill = 0
            for i in range(M):
                for j in range(M):
                    kill += arr[x+i][y+j]
            if kill > max_kill:
                max_kill = kill

    print(f'#{tc} {max_kill}')

