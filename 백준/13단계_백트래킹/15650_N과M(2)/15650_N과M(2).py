
import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    n, m = map(int, input().split())
    # print(f'#{tc} {n} {m}')

    lst = []
    def dfs(start):
        if len(lst) == m:
            print(' '.join(map(str,lst)))
            return

        for i in range(start, n+1):
            if i not in lst:
                lst.append(i)
                dfs(i+1)
                lst.pop()

    dfs(1)
