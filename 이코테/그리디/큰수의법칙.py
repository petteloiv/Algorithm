import sys
sys.stdin = open('input.txt')

n,m,k = map(int, input().split())
numbers = list(map(int, input().split()))

numbers.sort()
max1 = numbers[-1]
max2 = numbers[-2]
total = 0
now = 1

while True :

    if m >= k and now == 1:
        total += max1*k
        m -= k
        now = 2
    elif m >= k and now == 2:
        total += max2
        m -= 1
        now = 1
    elif m < k and now == 1:
        total += max1*m
        break
    elif m < k and now == 2 :
        total += max2
        m -= 1
        now = 1

print(total)
