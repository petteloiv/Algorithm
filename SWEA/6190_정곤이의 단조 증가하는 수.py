# ----------solved----------------#

import sys
sys.stdin=open("input.txt")

def Danzo(n):
    a = 10
    while n > 0:
        if n%10 <= a:
            a = n%10
            n = n //10
        else:
            return 0
    if n == 0:
        return 1


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    max_danzo = 0
    for i in range(len(numbers)-1):
        for j in range(i+1, len(numbers)):
            if Danzo(numbers[i] * numbers[j]) == 1:
                if numbers[i]*numbers[j] > max_danzo:
                    max_danzo = numbers[i]*numbers[j]

    if max_danzo == 0:
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max_danzo}')

print(Danzo(11))