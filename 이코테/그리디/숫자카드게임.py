import sys
sys.stdin=open('input.txt')

n,m = map(int,input().split())
numbers = []

for i in range(n):
    w = list(map(int, input().split()))
    numbers.append(w)

minnum = 0

for j in range(n):
    if minnum < min(numbers[j]):
        minnum = min(numbers[j])

print(minnum)
# print(numbers[1])