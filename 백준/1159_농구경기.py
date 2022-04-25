n = int(input())

names = list(input() for _ in range(n))
ans = []

for i in range(n):
    f = names[i][0]
    cnt = 0
    for j in range(n):
        if names[j][0] == f:
            cnt += 1
    if cnt >= 5:
        ans.append(f)

if len(ans) == 0:
    print('PREDAJA')
else:
    ans.sort()
    ans = set(ans)
    print(''.join(map(str,ans)))


# --------------------------------------------------------------------#

n = int(input())

firstnames = []

for i in range(n):
    name = input()
    firstnames.append(name[0])

ans = []

for i in firstnames:
    if firstnames.count(i) >= 5 and i not in ans:
        ans.append(i)

if len(ans) == 0:
    print('PREDAJA')
else:
    print(''.join(sorted(ans)))
