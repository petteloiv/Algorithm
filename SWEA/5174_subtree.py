# -------------------문제 정의 ----------------------#

# 자식 리스트 2개 만들기
# 중위순회 하면서 개수 세서 값 찾는 방식

# ---------------------------------알고리즘 풀이 ----------#
import sys
sys.stdin=open('input.txt')


# 중위순회
# 노드 개수 세기 ..
def in_order(node):
    global cnt
    if node:
        # 왼쪽 탐색
        in_order(lc[node])
        cnt+=1
        # 오른쪽 탐색
        in_order(rc[node])


T = int(input())

for tc in range(1,T+1):
    E, N = map(int, input().split())
    lst = list(map(int, input().split()))
    # print(lst)

    # 횟수 저장 변수, 왼쪽 자식, 오른쪽 자식 리스트
    cnt = 0
    lc = [0] * (E+2)
    rc = [0] * (E+2)

    # 입력받은 리스트 돌면서 자식 값 집어넣기
    for i in range(0,len(lst),2):
        parent = lst[i]
        child = lst[i+1]

        if lc[parent] == 0:
            lc[parent] = child
        else:
            rc[parent] = child

    # 중위 순회
    in_order(N)

    # 결과 담은 cnt 출력
    print(f'#{tc} {cnt}')