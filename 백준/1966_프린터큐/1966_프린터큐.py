
import sys
sys.stdin=open('input.txt')

# tc는 통과
# 백준 반례도 다 통과하는데 왜 틀렸는지 모르겠다..

'''
T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))

    out = []

    # 현재 위치
    now = [i for i in range(len(q))]

    cnt = 0

    while q:
        check = q.pop(0)
        nowplace = now.index(0)

        if len(q) == 0:
            out.append(check)
            cnt += 1
            now[nowplace] = cnt+1000000000

        for i in range(len(q)):
            if q[i] > check:
                q.append(check)
                now[nowplace] = len(q)
                for i in range(len(now)):
                    if now[i] > 1000000001:
                        continue
                    else:
                        now[i] = now[i] - 1
                break
            elif i == len(q)-1 and q[i] <= check:
                out.append(check)
                cnt += 1
                now[nowplace] = cnt+1000000000
                for i in range(len(now)):
                    if now[i] > 1000000001:
                        continue
                    else:
                        now[i] = now[i] - 1


    print(now[M] - 1000000000)
'''


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    q = list(map(int, input().split()))
    now = [i for i in range(len(q))]
    now[M] = 'target'

    cnt = 0

    while True:

        if q[0] == max(q):
            cnt += 1

            if now[0] == 'target':
                print(cnt)
                break

            else:
                q.pop(0)
                now.pop(0)

        else:
            q.append(q.pop(0))
            now.append(now.pop(0))

