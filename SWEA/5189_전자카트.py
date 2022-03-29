# -----------문제 정의 ------------#
# 시작, 끝 => 1
# 중간에 들어가는 부분집합 구하기
# 그 케이스들에 대해 값 구하고 ,,
# 최소값 찾기

# 여기는 가지치기를 어떻게 해줘야핮..?
# 더하는 중에 최소값 넘으면 멈추는걸로 처리하면 될까..?

# -------------------알고리즘 풀이 -------------------------#

import sys
sys.stdin=open('input.txt')
from itertools import permutations

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    # 2차원 배열에 0 안더해주고 그냥 숫자를 1씩 빼서 계산 ; 1-> 0, 2 -> 1 , ...
    # 부분집합 구하기 (순열,,)
    p = list(permutations([i for i in range(1, N)]))
    # [(1, 2), (2, 1)]
    # print(p)


    # 최소값 갱신해 줄 변수
    mincnt = 1000000

    for i in p:
        # 시작점 (행 좌표), 합
        s = 0
        cnt = 0
        for j in i:
            cnt += arr[s][j]
            # 만약 합이 최소합보다 크다면 break
            if cnt > mincnt:
                break
            # 다음 행 좌표가 된다..
            s = j

        # 맨 마지막에 다시 사무실로 돌아와야한다..
        cnt += arr[s][0]
        # 끝까지 돌았을 때의 합이 최소합보다 작다면 갱신
        if cnt < mincnt:
            mincnt = cnt

    print(f'#{tc} {mincnt}')

