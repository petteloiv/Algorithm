n = int(input())
num = list(map(int,input().split()))
money = int(input())

s = 0
e = max(num)

while s <= e:
    m = (s+e)//2
    cnt = 0
    for i in num:
        if i > m:
            cnt += m
        else:
            cnt += i
    if cnt <= money:
        s = m+1
    else:
        e = m-1

print(e)

