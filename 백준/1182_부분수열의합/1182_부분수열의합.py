import sys
sys.stdin=open('input.txt')

n, s = map(int, input().split())
lst = list(map(int, input().split()))

part = []
for i in range(1<<n):
    part1 = []
    for j in range(n):
        if i & (1<<j):
            part1.append(lst[j])
    part.append(part1)

# print(part)
cnt = 0
for i in part:
    if sum(i) == s and len(i) > 0:
        cnt += 1

print(cnt)