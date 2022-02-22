
# --------solved ----------#


import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N, K = map(int, input().split())
    yes = list(map(int, input().split()))

    lst = list(range(1,N+1))

    for i in range(len(yes)):
        lst.remove(yes[i])

    lst = ' '.join(map(str, lst))
    print(f'#{tc} {lst}')