

import sys
sys.stdin=open("input.txt")

# ---------------시간초과 --------------------#
queue = []
N = int(input())

for i in range(N):
    num = int(input())
    queue.append(num)
    queue.sort()

    if len(queue) % 2 == 1:
        print(queue[len(queue)//2])
    else:
        print(queue[len(queue)//2 -1])