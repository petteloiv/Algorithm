import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    word = input().split()
    # print(word)

    ans = ''

    for i in range(len(word)-1, -1, -1):
        ans += word[i]
        if i == 0:
            break
        ans += ' '

    print(f'Case #{tc}: {ans}')