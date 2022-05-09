# 시간초과나서 이진탐색으로 풀기

import sys
input = sys.stdin.readline

n = int(input())
cards = list(map(int,input().split()))
m = int(input())
num = list(map(int,input().split()))

cards.sort()


def Binary(target, check):
    start, end = 0, n
    while(start < end):
        mid = (start + end) // 2
        if check == 0:
            if cards[mid] < num:
                start = mid + 1
            else:
                end = mid
        else:
            if cards[mid] <= num:
                start = mid + 1
            else:
                end = mid
    return end

result = []
for i in num:
    result.append(Binary(i,1) - Binary(i,0))
print(*result)



