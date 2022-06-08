lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

a = int(input())

ans = []

for i in lst:
    if i % a == 0:
        ans.append(i)

print(ans)