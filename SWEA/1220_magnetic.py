import sys
sys.stdin=open("input.txt")

for tc in range(1,11):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    cnt = 0

    for j in range(N):
        stack = []
        for i in range(N):
            if arr[i][j] == 1:
                if len(stack) == 0:
                    stack.append(1)
                else:
                    continue
            elif arr[i][j] == 2:
                if len(stack) > 0 and stack[-1] == 1:
                    cnt += 1
                    stack.clear()
                    continue
                else:
                    continue
            else:
                continue

    print(F'#{tc} {cnt}')