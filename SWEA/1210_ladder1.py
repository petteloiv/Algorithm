# ------------------문제 정의 --------------------------#
# 규칙 없이 사다리 만들어짐

# --------------------알고리즘 풀이 ------------#

import sys
sys.stdin = open("input.txt.txt")

T = 10

for tc in range(1,T+1):
    # 테스트케이스 번호
    tc = int(input())
    # 인풋받은 값 .,. 100 * 100 배열 만들기
    arr = [list(map(int, input().split())) for _ in range(100)]

    dm = [0, 1, 0] # 아래
    dn = [1, 0, -1] # 좌우

    # 1. 첫번째의 아래 값이 1이 아니면 continue
    # 2. 첫번째 아래 값이 1이면 그때 반복문 ..

    for i in range(100):
        # 시작값과 그 아래 값이 1일때 ! (이 두개가 1이 되지 않으면.. 성립하지않는다)
        while arr[0][i] == 1 and arr[1][i] == 1:
            # 시작위치 설정
            m,n = 1, i
            # m과 n의 범위를 종료조건으로 설정
            while 0 <= m < 100 and 0 <= n < 100:
                for j in range(3): # 현재 우선 순위 오른쪽, 아래, 왼쪽 순서 ..
                    nm = m + dm[j]
                    nn = n + dn[j]
                    # 새로운 좌표값이 2일때 (도착)
                    if arr[nm][nn] == 2:
                        print(i)
                    # 좌표들 범위 안에 있고 값이 1 일때 (이동 가능)
                    elif 0 <= nm < 100 and 0 <= nn < 100 and arr[nm][nn] == 1:
                        # 현재 위치 변화! 이동 ...
                        m,n = nm, nn
                    # 다 아닐때 ,,, 0 (해당사항 없다, 건너뛰기)
                    else:
                        continue
        # 시작값, 그 아래값 1 아니면 그냥 건너뛰기
        else:
            continue
