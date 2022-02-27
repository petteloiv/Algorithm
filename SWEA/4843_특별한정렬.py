import sys
sys.stdin=open("input.txt")

T = int(input())

for tc in range(1,T+1):
    N = int(input())
    numbers = list(map(int, input().split()))

    numbers.sort()

    ans = []
    for i in range(5):
        ans.append(numbers.pop())
        ans.append(numbers.pop(0))

    ans = ' '.join(map(str, ans))
    print(f'#{tc} {ans}')