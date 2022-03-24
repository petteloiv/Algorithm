
# 16진수 -> 2진수로 표현

import sys
sys.stdin=open('input.txt')

T = int(input())

for tc in range(1,T+1):
    N, word = map(str, input().split())
    # print(N, '*', word)

    ans = ''
    for i in range(len(word)):
        # 16진수를 10진수로 변환하기
        tmp = int(word[i], 16)
        # 10진수를 2진수로 변환
        # 맨 앞에 붙는 0b 공백으로 바꿔주기
        tmp = bin(tmp).replace('0b','')
        # 길이 맞춰줘야한다.. 길이가 4 아니면 앞에 0 추가해주기
        while len(tmp) != 4:
            tmp = '0' + tmp
        ans += tmp

    print(f'#{tc} {ans}')