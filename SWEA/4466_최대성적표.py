
import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    scores = list(map(int, input().split()))

    for j in range(N):
        for i in range(0, N-j-1):
            if scores[i] > scores[i+1]:
                scores[i], scores[i+1] = scores[i+1], scores[i]

    top_K = scores[N-K:N]
    total = 0
    for i in top_K:
        total +=i

    print(f'#{tc} {total}')
