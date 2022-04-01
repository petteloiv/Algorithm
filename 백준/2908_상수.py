

lst = list(map(str, input().split()))

a1 = lst[0][::-1]
a2 = lst[1][::-1]

if a1 > a2:
    print(a1)
else:
    print(a2)