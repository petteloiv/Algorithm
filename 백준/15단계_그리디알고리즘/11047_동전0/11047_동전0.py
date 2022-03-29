import sys
sys.stdin=open('input.txt')

# n 동전 종류 k 구할 돈 ... 가치 합
N, K = map(int, input().split())
coin = [int(input()) for _ in range(N)]

cnt = 0
for i in range(len(coin)-1,-1,-1):
    if K >= coin[i]:
        n =  K // coin[i]
        cnt += n
        K = K - (coin[i]*n)

print(cnt)

