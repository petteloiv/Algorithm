

import sys
sys.stdin=open("input.txt")

# ---------------시간초과 --------------------#
# queue = []
# N = int(input())
#
# for i in range(N):
#     num = int(input())
#     queue.append(num)
#     queue.sort()
#
#     if len(queue) % 2 == 1:
#         print(queue[len(queue)//2])
#     else:
#         print(queue[len(queue)//2 -1])

# -----------------이진탐색 사용----------------------#

# 넣을 위치 찾기
def Search(k):
    global lst
    # 왼쪽 시작점 , 오른쪽 끝 위치 설정
    left = 0
    right = len(lst)-1

    while left<=right:
        # 중간위치
        mid = (left+right)//2

        # 입력값 = 중간값 => 중간값
        if k == lst[mid]:
            return mid

        # 입력값 < 중간값
        # 오른쪽 끝을 중간값 -1 로 설정하고 다시 돌리기
        if k < lst[mid]:
            right = mid-1

        # 입력값 > 중간값
        # 시작점을 중간값 +1 설정하고 다시 돌리기
        else:
            left = mid+1

    return left

N = int(input())


lst  = []
for i in range(N):
    num = int(input())
    # 리스트 비어있으면 리스트에 추가
    if len(lst)==0:
        lst.append(num)
    # 리스트에 숫자가 있으면
    # 이진탐색 돌려서 숫자 넣을 위치 찾기
    # 그 위치에 넣어주기
    else:
        where = Search(num)
        lst.insert(where,num)

    # 리스트 짝수일 때 가운데 값 중 작은값
    if len(lst)%2==0:
        result = lst[len(lst)//2-1]
    else:
        # 홀수일 때 중간값
        result = lst[len(lst)//2]


    print(result)