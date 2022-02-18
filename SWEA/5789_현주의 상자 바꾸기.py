# ------------------문제 정의 ------------------------#

# 1. 인덱스 그리기  (N개짜리)
# i (1<=i<=Q)
# l번 상자 ~ r번 상자까지의 값을 i로 변경
# 인덱스 직관적으로 작성하는게 좋다 ex) l-2 , r -1

# --------알고리즘 풀이  -----------#

import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, Q = map(int, input().split())
    arr = [0]*(N+1)

    for i in range(1,Q+1):
        L, R = map(int,input().split())
        for j in range(L, R+1):
            arr[j] = i

    total = ' '.join(map(str,arr[1:]))
    print(f'#{tc} {total}')
