a = []

for i in range(6):
    b = input('Element? ')
    a.append(b)


# 홀수번째 원소가 앞 , 짝수번째 원소가 뒤...

lst = []

for i in range(1,6,2):
    lst.append(a[i])

for i in range(0,6,2):
    lst.append(a[i])

print(lst)