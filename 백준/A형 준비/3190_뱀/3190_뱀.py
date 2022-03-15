# 문제 정의
#  사과를 먹으면 뱀 길이 늘어남
# 벽 / 자기 자신의 몸과 부딪히면 게임 끝
# 게임이 몇 초에 끝나는지 출력

# ----------모르겠는점 ---------------#
# 방향 설정하는게 좀 어렵다
# 델타로 어떻게든 해결해보기
# 시작점이 1행 1열이다 .. 0행 0열로 시작하는데 좌표 설정

import sys
sys.stdin=open("3190.txt")

# -------------------------------------런타임에러 ----------------------------#

T = int(input())

for tc in range(1, T+1):
    # 보드 크기
    N = int(input())
    # 사과의 개수
    K = int(input())
    # 사과의 위치
    apple = list(list(map(int,input().split())) for _ in range(K))
    # 방향 변환 횟수
    L = int(input())
    # 방향 변환 정보
    direction = list(list(map(str,input().split())) for _ in range(L))

    arr = list([0]*N for _ in range(N))
    # print(arr)
    # print(apple)
    # print(direction)
    dtime = []
    dway = []
    for i in direction:
        dtime.append(int(i[0]))

    for i in direction:
        dway.append(i[1])

    # print(dtime, dway)


    # 사과 있는 위치 1로 바꾸기
    for i in apple:
        arr[i[0]][i[1]] = 1

    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    snake = []
    sec = 0
    # 출발좌표
    i = j = 0
    # 이동방향 (시작 -> 오른쪽)
    d = 0
    ci = di[d]
    cj = dj[d]
    # 뱀.. 큐..?에 시작 좌표 추가
    snake.append([i,j])

    while 0 <= i < N and 0 <= j < N:
        # 도착한 지점에 사과가 있을 경우
        if 0 <= i+ci < N and 0 <= j+cj < N and arr[i + ci][j + cj] == 1:
            sec += 1
            arr[i+ci][j+cj] = 4
            # 뱀 ... 길이.. snake 스택에 추가
            snake.append([i+ci, j+cj])
            # 방향 바꾸는 시간에 해당될 경우
            # if sec in direction:
            # #방향 변경 .. L, R 따라서
            if sec in dtime:
                ind = dtime.index(sec)
                # 오른쪽으로 90
                if dway[ind] == 'D':
                    d = (d+1) % 4
                # 왼쪽으로 90
                else:
                    d = (d+3) % 4
            i = i+ci
            j = j+cj
            ci = di[d]
            cj = dj[d]
            continue
        # 사과 없는 경우 -> 뱀 하나씩 당겨야한다...
        elif 0 <= i+ci < N and 0 <= j+cj < N and arr[i + ci][j + cj] == 0:
            sec += 1
            # 뱀 하나씩 당기기 .. 이동한 자리 0 으로 변경시키기
            r = snake.pop(0)
            arr[r[0]][r[1]] = 0
            arr[i + ci][j + cj] = 4
            snake.append([i + ci, j + cj])
            # 얘도 방향
            if sec in dtime:
                ind = dtime.index(sec)
                # 오른쪽으로 90
                if dway[ind] == 'D':
                    d = (d+1) % 4
                # 왼쪽으로 90
                else:
                    d = (d+3) % 4
            # 시작위치 변경해주기
            i = i+ci
            j = j+cj
            ci = di[d]
            cj = dj[d]
            continue
        else:
            sec += 1
            print(f'#{tc} {sec}')
            break



