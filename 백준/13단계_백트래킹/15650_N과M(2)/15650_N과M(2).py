
import sys
sys.stdin=open('input.txt')


def dfs(start):
    if len(lst) == m:
        print(' '.join(map(str, lst)))
        return

    # 여기서 시작점을 start로 준다! 중복 막기 위해서 ..
    for i in range(start, n + 1):
        if i not in lst:
            lst.append(i)
            dfs(i + 1)
            lst.pop()


n, m = map(int, input().split())
# print(f'#{tc} {n} {m}')

lst = []

dfs(1)
