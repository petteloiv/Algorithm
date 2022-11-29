# 도현이의 집 N개가 수직선 위에 있다 도현이는 부자구나..
# 집 좌표 : x1, x2, ..., xn (같은 좌표 가질 일은 없당)
# 집에 공유기 C개 설치
# 한 집에 공유기 하나만 설치 가능
# 가장 인접한 두 공유기 사이의 거리를 가능한 크게~
# C개의 공유기 N개의 집에 적당히 설치
# -> 가장 가까운 두 공유기 사이의 거리를 최대로 (최대 거리 출력)

# input)
# N C
# Xi
# ....
# N개 ..

# 이거를 이진탐색으로 어케 풀지?
# 공유기 쭉 설치하고 ..
# 공유기 설치 위치 말고 공유기 사이의 거리 체크하기

import bisect
import sys

N, C = map(int,sys.stdin.readline().split())
house = []
for _ in range(N):
    house.append(int(sys.stdin.readline()))
house.sort()

# 일단 ,, 집 정렬했는디 ,,..
# 가장 작은 간격 : 1
# 가장 넓은 간격 : 끝에서 끝 ..
# 시작점, 끝점으로 잡는당
start = 1
end = house[-1] - house[0]

while True:
    mid = start + end // 2

    # 시작 위치 & 시작 인덱스 (둘 다 0부터), 공유기 개수
    start_position = house[0]
    start_index = 0
    wifi_cnt = 0

    # 집 개수보다 작을 때
    while start_index < N:
        wifi_cnt += 1
        start_index = bisect.bisect_left(house, house[start_index] + mid)

    # 설치 C보다 적게 가능 == 설치 거리 너무 멀다 ㅜ
    # 가능한 최소 거리 1씩 줄이기 ..
    if wifi_cnt < C:
        end = mid - 1

    # 설치 C보다 많이 가능 == 더 늘려서 설치 가능
    # 1씩 늘리기
    elif wifi_cnt >= C:
        start = mid + 1

    if mid == end:
        print(mid)
        break
