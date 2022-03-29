# --------- 문제 정의 --------------#
# 오른쪽, 아래로만 이동 가능
# 끝까지 도착하고 mincnt와 비교 ..
# 계산 중간에 값이 mincnt보다 커지면 멈추고 돌아가기
# dfs 사용하는 것 같은데 ,...
# 어디로 돌아가야하지..? 어떻게 돌리지... ? .. 난 바보였다 재귀니까 리턴시키면 된다


# -----------------------알고리즘 풀이 ----------------------#

import sys
sys.stdin=open('input.txt')

# 오른쪽, 아래쪽
di = [0, 1]
dj = [1, 0]

# dfs..
def Dfs(i, j, cnt):
    global mincnt

    # 방문 지점 값 cnt에 더해주기
    cnt += arr[i][j]

    # 도착지점에 왔으면,,
    # 최소값 확인하기
    if i == N-1 and j == N-1:
        if cnt < mincnt:
            mincnt = cnt
        return

    # 도착지점에 아직 안 왔는데 최소값보다 커질 경우
    elif i < N-1 and j < N-1 and cnt > mincnt:
        return

    # 델타 돌리기.. 빙빙..
    for d in range(2):
        ni = i + di[d]
        nj = j + dj[d]
        if 0<=ni<N and 0<=nj<N:
            Dfs(ni,nj,cnt)


T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int,input().split())) for _ in range(N)]
    # print(arr)

    # 비교해 줄 최소합, 이동거리 합 변수
    mincnt = 1000
    cnt = 0

    # 함수 돌리기..
    Dfs(0,0,cnt)
    print(f'#{tc} {mincnt}')