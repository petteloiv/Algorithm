# --------------- 문제 정의 --------------------#

# 100 * 100 의 2차원 배열 주어짐
# 각 행의 합, 각 열의 합, 각 대각선의 합 중 최댓값 구하는 프로그램

# 총 1개의 테스트 케이스
# 배열 크기는 100 * 100
# 각 행의 합은 integer 범위 넘지 않는다 ... 일단 값이 나오는 애들이다..
# 동일한 최댓값이 있을 경우, 하나의 값만 출력한다

# 출력 : #tc 답

# ------------------알고리즘 풀이 ----------------#

# 일단 테스트케이스 받아서 배열로... 조지기 ..

import sys
sys.stdin = open('input.txt')

for tc in range(10):
    T = int(input())

    arr = []
    for i in range(100):
        arr.append(list(map(int, input().split())))
        # print(arr)

    # 행 우선 순회
    max_n = 0
    for i in range(100) :
        total = 0
        for j in range(100):
            total += arr[i][j]
        if total > max_n:
            max_n = total

    # 열 우선 순회
    max_yeol = 0
    for i in range(100):
        total = 0
        for j in range(100):
            total += arr[j][i]
        if total > max_yeol:
            max_yeol = total

    # 대각선 순회 ... (1,1) (2,2) x = y 왼 - > 오
    max_d = 0
    for i in range(100):
        total = 0
        for j in range(100):
            if i == j:
                total += arr[i][j]
        if total > max_d:
            max_d = total

    # 대각선 순회 오-> 왼 (100,0) (99,1) 이런식이다 ...
    max_r = 0
    for i in range(100):
        total = 0
        for j in range(100, -1):
            total += arr[i][j]
            if total > max_r:
                max_r = total


    best = 0
    numb = [max_n, max_r, max_d, max_yeol]

    for i in range(len(numb)):
        if numb[i] > best:
            best = numb[i]

    print(f'#{tc+1} {best}')








