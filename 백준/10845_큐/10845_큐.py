# 18258 큐2 -> 시간제한 1초였는데
# 얘는 0.5초다 ,,, input() 어떻게든 처리해줘야할거같고


import sys
sys.stdin=open('input.txt')

from collections import deque

input = sys.stdin.readline
# 명령의 수
N = int(sys.stdin.readline())

q = deque()

for i in range(N):
    a = sys.stdin.readline().split()
    if a[0] == 'push':
        q.append(a[1])
    elif a[0] == 'front':
        if len(q) != 0:
            print(q[0])
        else:
            print(-1)
    elif a[0] == 'back':
        if len(q) != 0:
            print(q[-1])
        else:
            print(-1)
    elif a[0] == 'size':
        print(len(q))
    elif a[0] == 'pop':
        if len(q) != 0:
            print(q.popleft())
        else:
            print(-1)
    elif a[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)