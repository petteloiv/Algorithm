n = int(input())

num = list(map(int, input().split()))
num.sort()

if n == 1:
    print(n*n)
else:
    minnum = min(num)
    maxnum = max(num)
    print(num[0] * num[-1])