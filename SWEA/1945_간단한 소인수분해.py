import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0

    while 2<= N <=10000000 :
        if N % 11 == 0:
            e += 1
            N = N/11
        elif N % 7 == 0:
            d += 1
            N = N//7
        elif N % 5 == 0:
            c += 1
            N = N//5
        elif N % 3 == 0:
            b += 1
            N = N//3
        elif N % 2 == 0:
            a += 1
            N = N//2
    print(f'#{tc} {a} {b} {c} {d} {e}')



