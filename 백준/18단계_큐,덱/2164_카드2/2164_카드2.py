import sys
sys.stdin=open('input.txt')
from collections import deque

N = int(input())

q = deque()

# 카드 큐에 집어넣기
for i in range(N):
    q.append(i)

# 반복을 하자 ..
while len(q) > 1:
