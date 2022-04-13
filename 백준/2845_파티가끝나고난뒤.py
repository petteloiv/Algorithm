l, p = map(int, input().split())

real = l*p

lst = list(map(int, input().split()))

for i in range(len(lst)):
    if i == len(lst)-1:
        print(i-real)
    else:
        print(i-real, end=' ')