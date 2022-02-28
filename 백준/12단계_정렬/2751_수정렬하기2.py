# 버블정렬로 안돌아가는거같다 ..?

N = int(input())

num = []
for i in range(N):
    num.append(int(input()))

num.sort()


for j in num:
    print(j)