from itertools import combinations

n = int(input())
s = list(map(int, input().split()))

ans = []

for i in range(1, n+1):
    part = list(combinations(s,i))
    for j in part:
        ans.append(sum(j))

ans = list(set(ans))
ans.sort()

cnt = 1
for i in ans:
    if i!= cnt:
        break
    cnt += 1

print(cnt)



