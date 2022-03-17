# ------------문제 정의 --------------------#
# 왜...제한시간 초과가 나지 ㅠ

# --------------알고리즘 풀이 ------------------------#
import sys
sys.stdin=open('input.txt')

# ---------------------- 10개 중 9개 ----------------------#
# visited에 좌표를 다 입력하고 확인하게 하는게 오래 걸리는 것 같다 ...
# visited를 2차원 배열로 변경하고 값 비교로 바꿨더니 패스
# -----------------------pass -------------------------------#
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    maze = list(list(map(int,input())) for _ in range(N))

    q = []
    visited = [[0]*N for _ in range(N)]
    ans = 0
    distance = [[0]*N for _ in range(N)]
    di = [1, -1, 0, 0]
    dj = [0, 0, 1, -1]
    si = sj = 0

    # 출발점 찾기
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                si = i
                sj = j

    q.append([si, sj])
    visited[si][sj] = 1

    while q:
        si, sj = q.pop(0)

        for d in range(4):
            ni = si + di[d]
            nj = sj + dj[d]

            if 0<=ni<N and 0<=nj<N and (maze[ni][nj] == 0 or maze[ni][nj] == 3) and visited[ni][nj] == 0:
                if maze[ni][nj] == 0:
                    q.append([ni, nj])
                    visited[ni][nj] = 1
                    distance[ni][nj] = distance[si][sj] + 1
                else:
                    ans = distance[si][sj]
                    break

    print(f'#{tc} {ans}')
