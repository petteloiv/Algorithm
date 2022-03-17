# BFS 사용
# 출발점 -> 도착지점까지 갈 수 있는 길이 있는지!
# arr 크기 16*16
#  0 : 통로 1 : 벽 2: 도착 3: 출발

# ---------------------알고리즘 풀이 --------------------#

import sys
sys.stdin=open("input.txt")

for t in range(1,11):
    tc = int(input())
    maze = list((list(map(int,input())) for _ in range(16)))
    # 방문 여부 저장
    visited = []
    # 큐
    q = []
    # 출력할 값 (길 여부)
    route = 0

    # 탐색..
    di = [1, -1, 0, 0]
    dj = [0, 0, -1, 1]

    # 시작점 0으로 임의 설정
    si = sj = 0
    # 시작점 찾기 (3인 값 저장)
    for i in range(16):
        for j in range(16):
           if maze[i][j] == 3:
               si = i
               sj = j

    # 최초 시작점 q, visited에 저장
    q.append([si,sj])
    visited.append([si,sj])

    # 큐 비어있지 않은 동안..
    while q:
        # deQueue 한 값을 출발지점으로 지정,,,
        start = q.pop(0)
        si = start[0]
        sj = start[1]

        # 상하좌우 탐색하면서
        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]

            # 범위 안에 있고, 값이 0이거나 2이고, visited에 없으면
            if 0<=ni<16 and 0<=nj<16 and (maze[ni][nj] == 0 or maze[ni][nj] == 2) and [ni, nj] not in visited:
                # 값이 2이면 도착 (길 있음) => route 1로 바꾸고 종료
                if maze[ni][nj] == 2:
                    route = 1
                    break
                # 이외 : 통로일 경우 ... 큐, 방문에 추가하기
                else:
                    q.append([ni,nj])
                    visited.append([ni,nj])

    print(f'#{tc} {route}')
