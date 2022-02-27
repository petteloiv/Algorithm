
import sys
sys.stdin=open("input.txt")

def Hamsu(A, N, B, M):
    max_sum = 0
    for i in range(M - N + 1):
        total = k = 0
        for j in range(i, i + N):
            total += (B[j] * A[k])
            if k == N:
                break
            k += 1
        if total > max_sum:
            max_sum = total
    return max_sum



# ------------ 5개 맞았다.. 분명 어디서 조건 빼놓은것 ---------------#
T = int(input())

for tc in range(1,T+1):
    nlst1, mlst2 = map(int, input().split())
    lst1 = list(map(int, input().split()))
    lst2 = list(map(int, input().split()))

    if nlst1 > mlst2:
        A = lst2
        N = mlst2
        B = lst1
        M = nlst1
    else:
        A = lst1
        N = nlst1
        B = lst2
        M = mlst2

    print(f'#{tc} {Hamsu(A, N, B, M)}')


# 더 긴 쪽이 B 더 짧은 쪽이 A