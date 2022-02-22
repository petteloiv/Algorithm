# --------- 문제 정의 ----------------#
# 난 수학이 정말 싫다 ...
# 크기가 N인 파스칼의 삼각형 만들기
# 파스칼 삼각형 규칙
# 1. 첫번째 줄은 항상 숫자 1
# 2. 두번째 줄부터 각 숫자들 = 왼쪽 + 오른쪽 위 숫자

# N이 4일 경우 ...
# [[1],[1,1],[1,2,1],[1,3,3,1]]

# ----------알고리즘 설명 ----------------#

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    # print(arr)

    for i in range(N):
        for j in range(0, i+1):
            if j == 0 or j == i:
                arr[i][j] = 1
            else:
                arr[i][j] = arr[i-1][j-1] + arr[i-1][j]


    print(f'#{tc}')
    for i in range(len(arr)):
        print(' '.join(map(str, arr[i][:i+1])))


