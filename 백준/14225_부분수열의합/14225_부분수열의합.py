import sys
sys.stdin=open('input.txt')

n = int(input())
lst = list(map(int, input().split()))

add = []
for i in range(1<<n):
    part = []
    for j in range(n):
        if i & (1<<j):
            part.append(lst[j])
    add.append(sum(part))

for i in range(1,1000000000000):
    if i not in add:
        print(i)
        break

