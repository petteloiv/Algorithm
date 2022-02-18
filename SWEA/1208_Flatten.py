# -----------------문제 정의 -------------#
# 노란색 상자들이 쌓여있다 ...
# 평탄화 => 높은 곳의 상자 -> 낮은 곳으로 옮기기 .. (최고점과 최저점 간격 줄이기)
# after 평탄화, 가장 높은 곳 - 가장 낮은 곳 <= 1
# 작업 횟수 제한 O..
# 제한된 횟수만큼 작업 한 후 최고점-최저점 차이 반환

# 1. 버블정렬 함수로 만들기
# 2. 가장 큰 값 [-1] 에서 1 빼고 가장 작은 값 [0] 에 1 더해주기
# 3. 다시 bubblesort로 평탄화.. 반복 (dump만큼)

# ----------- 알고리즘 풀이 ------------#

import sys
sys.stdin = open('input.txt')

# 버블정렬 함수 ..
def BubbleSort(a):
    for i in range(len(a)-1, 0 , -1):
        # 인덱스 0~i 범위 안에서 반복
        for j in range(0, i):
            # 크기 비교 .. j > j+1 이라면 두 개의 값을 바꿔준다
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
        return(a)

# 테스트 케이스만큼 순회 ..
for tc in range(1,11):
    dump = int(input())
    height = list(map(int, input().split()))

    # 버블소트 함수 실행하고 최대 -1 최소 +1 하면서 평탄화 시키기
    # dump만큼~~~~
    for i in range(dump):
        BubbleSort(height)
        height[0] += 1
        height[-1] -= 1

    BubbleSort(height)
    result = height[-1] - height[0]
    print(f'#{tc} {result}')


# -------------첫 시도 (오류) ---------------#
# 범위를 어떻게 잡아야할 지 몰랐다 ..

    # # dump가 1 이상일 때
    # while dump > 1:
    #     # for i in range(1,dump+1):
    #         # 버블 정렬
    #     for i in range(len(height) - 1, 0, -1):
    #         # 인덱스 0~i 범위 안에서 반복
    #         for j in range(0, i):
    #             # 크기 비교 .. j > j+1 이라면 두 개의 값을 바꿔준다
    #             if height[j] > height[j + 1]:
    #                 height[j], height[j + 1] = height[j + 1], height[j]
    #             # print(height)
    #         # 정렬 끝 ..
    #         # max - min 차가 1 이하이면 프린트 (평탄화완료 .. )
    #         if height[-1] - height[0] <= 1:
    #             print(f'#{tc} {height[-1] -  height[0]}')
    #         # 아니면 max에서 min으로 1 준다 ..
    #         else:
    #             # 한번 옮겼으니까 dump -1
    #             height[-1] -= 1
    #             height[0] += 1
    #             dump -= 1
    # if dump <= 1:
    #     print(f'#{tc} {height[-1] - height[0]}')