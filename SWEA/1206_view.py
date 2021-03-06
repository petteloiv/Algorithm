#---------------1. 문제 정의-------------------#

# input 첫 줄 = 가로 길이
# input 두번째 줄 = 건물의 높이 값 (건물이 몇 층인가?!) => 1차원 배열 형태로 준다
# 한꺼번에 처리 불가. 값 하나하나 비교하면서 판단해야한다!
# 단위 작업 (1개) 반복!!!!!

# i : 조사할 빌딩의 idx
# 왼, 오른쪽 2개씩 구하기 .. i-2 i-1 i i+1 i+2
#  조사할 범위 (2 ~ N-3) 설정하고 작업 반복! (좌우로 2칸 끝 공백 존재하기 때문에)
# 가장 큰 값이 중요 ... 가장 큰 값으로 비교하면 됨.
# 이해 했음!!!! 양쪽 두개 (총 4개) 빌딩 높이 다 구해서 최댓값과
# 원래 빌딩 높이 비교. 원래 높이 - 최댓값 == 조망권 확보된 세대수


# ---------------2. 알고리즘 설명 ------------------#
import sys
sys.stdin = open('input.txt')

# 총 테스트 케이스에 대해 반복
for tc in range(10):
    # 가로 길이 .. 땅 넓이?
    N = int(input())
    # 각 빌딩들의 높이 리스트로 변환 ..
    arr = list(map(int, input().split()))

    # 층수를 누적할 변수
    ans = 0
    # 모든 빌딩에 대해 조망권이 확보된 세대수를 계산
    # 2 ~ N-3 (양쪽 끝 2개는 건물 없음! 건물 시작 ~ 건물 끝 돌리기)
    for i in range(2, N - 2):
        # i번 빌딩의 조망권 계산
        # [i-2],[i-1], [i+1],[i+2]
        # max 사용금지 ,..
        max_val = arr[i-2]
        if max_val < arr[i -1]:
            max_val = arr[i - 1]
        if max_val < arr[i + 1]:
            max_val = arr[i+1]
        if max_val < arr[i+2]:
            max_val = arr[i+2]

        if arr[i] > max_val:
            ans += arr[i] - max_val

    print(f'# {tc+1} {ans}')