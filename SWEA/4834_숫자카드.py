import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1, T + 1):
    N = int(input())
    num = list(map(int, input()))
    cnt = [0] * 10

    for i in range(N):
        cnt[num[i]] += 1

    max_idx = 0
    max_count = 0

    for i in range(10):
        if cnt[i] >= max_count:
            max_count = cnt[i]
            max_idx = i

    print(f'#{tc} {max_idx} {max_count}')