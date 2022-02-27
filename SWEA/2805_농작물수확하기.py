
import sys
sys.stdin=open("input.txt")

# ---------------------50개 중 6개 맞음 -------------------#
# trial 2. 50개 중 5개


# T = int(input())
#
# for tc in range(1,T+1):
#     N = int(input())
#     arr = [list(map(int, input())) for _ in range(N)]
#
#     total = 0
#     middle = N //2
#
#     # 1. 0 ~ N//2 전까지
#     for i in range(middle):
#         for j in range(i+1):
#             if i == 0:
#                 total += arr[i][middle]
#             else:
#                 total += arr[i][middle + j]
#                 total += arr[i][middle - j]
#
#
#     # 2. 중간 열!
#     for j in range(N):
#             total += arr[middle][j]
#
#     # 3. 중간 이후 ~ 끝 열
#     for i in range(middle+1, N):
#         for j in range(N-i):
#             if i == N-1:
#                 total += arr[i][middle]
#                 break
#             else:
#                 if j < N:
#                     total += arr[i][j]
#
#     print(f'#{tc} {total}')


# -----------------2. 답지 한번 보고 .. 따라가기 ---------------#

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    arr = [list(map(int, input())) for _ in range(N)]

    middle = N//2
    s = e = middle
    cnt = 0

    for i in range(N):
        for j in range(s, e+1):
            cnt += arr[i][j]
        if i < middle:
            s -= 1
            e += 1
        else:
            s += 1
            e -= 1

    print(f'#{tc} {cnt}')

