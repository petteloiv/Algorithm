


# ---------------------- 계속 틀렸으니 얘는 다시 확인 필요 ------------------#


import sys
sys.stdin=open('input.txt')
from collections import deque

N, K = map(int, input().split())

lst = deque()
for i in range(1, N+1):
    lst.append(i)
# print(lst)


print('<', end='')

while lst:
    for i in range(N-1):
        lst.append(lst[0])
        lst.popleft()
    print(lst.popleft(), end='')
    if lst:
        print(',', end='')
print('>')



#
# print('<', end='')
# while s:
#     for i in range(k - 1):
#         s.append(s[0])
#         s.popleft()
#     print(s.popleft(), end='')
#     if s:
#         print(', ', end='')
# print('>')

# n, k = map(int, input().split())
# q = [i for i in range(1,n+1)]
# print("<",end='')
# i = 0
#
# while len(q) > 1:
#     i = i+k
#     if i > len(q):
#         i = i % len(q)
#         if i == 0 :
#             i = i+ len(q)
#     i = i-1
#     print(str(q.pop(i)), end=", ")
#
# print("{}>".format(str(q.pop())))