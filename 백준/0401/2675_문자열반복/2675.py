
import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, str = input().split()
    N = int(N)

    ans = []
    for i in range(len(str)):
        for j in range(N):
            ans.append(str[i])

    ans = ''.join(ans)

    print(ans)

